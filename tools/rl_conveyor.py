#!/usr/bin/env python3
"""Fail-closed, non-promoting utilities for the RL research conveyor."""

import argparse
import base64
import binascii
import hashlib
import json
import os
import re
import shlex
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from rl_catalog import (
    CatalogError,
    parse_rl_identifier,
    query_results,
    query_sessions,
    validate_indexes,
    write_indexes,
)

ROOT = Path(__file__).resolve().parents[1]
AUTH = ROOT / "authoritative"
GIT_TIMEOUT_SECONDS = 30
RECONSTRUCTION_TIMEOUT_SECONDS = 60
VERIFIER_TIMEOUT_SECONDS = 120
DIRECT_TREE_TRANSPORT = "direct Git tree plus deterministic ZIP reconstruction"
DIRECT_TREE_MANIFEST_FIELDS = {
    "canonical_zip",
    "canonical_zip_sha256",
    "completed_package_tree_sha",
    "completed_rl",
    "incoming_rl",
    "incoming_rl_started",
    "reconstruction_script",
    "transport",
}


class Failure(RuntimeError):
    pass


def git(*args, timeout=GIT_TIMEOUT_SECONDS):
    try:
        run = subprocess.run(
            ["git", *args], cwd=ROOT, text=True, capture_output=True, timeout=timeout
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise Failure("git command failed: %s" % error) from error
    if run.returncode:
        raise Failure(run.stderr.strip() or "git command failed")
    return run.stdout


def _git_bytes(*args, timeout=GIT_TIMEOUT_SECONDS):
    try:
        run = subprocess.run(
            ["git", *args], cwd=ROOT, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise Failure("git command failed: %s" % error) from error
    if run.returncode:
        message = run.stderr.decode("utf-8", errors="replace").strip()
        raise Failure(message or "git command failed")
    return run.stdout


def _optional_git(*args):
    try:
        return git(*args).strip()
    except Failure:
        return None


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def safe(name):
    if not isinstance(name, str) or not name or "\0" in name or "\\" in name:
        raise Failure("unsafe bundle/manifest path: %r" % name)
    raw_parts = name.split("/")
    if any(part in {"", ".", ".."} for part in raw_parts):
        raise Failure("unsafe bundle/manifest path: %r" % name)
    path = PurePosixPath(name)
    if path.is_absolute() or re.fullmatch(r"[A-Za-z]:", raw_parts[0]):
        raise Failure("unsafe bundle/manifest path: %r" % name)
    return Path(*path.parts)


def safe_manifest_path(name):
    """Accept the checksum convention './path' without erasing traversal."""
    if isinstance(name, str) and name.startswith("./"):
        name = name[2:]
    return safe(name)


def state():
    if not AUTH.is_dir():
        raise Failure("authoritative/ is missing")
    files = [p for p in AUTH.rglob("*") if p.is_file()]
    # Authoritative handovers are extracted below one package directory; the
    # target is therefore nested rather than a top-level authority file.
    targets = sorted(AUTH.rglob("*TARGET*.md"))
    bundles = sorted(AUTH.glob("*.zip"))
    sidecars = sorted(AUTH.glob("*.zip.sha256"))
    if len(targets) != 1 or len(sidecars) != 1:
        raise Failure("expected one target, one bundle sidecar, and an RL number in authoritative/")
    target_numbers = {int(value) for value in re.findall(r"RL(\d+)", targets[0].name, re.I)}
    if len(target_numbers) != 1:
        raise Failure("the unique authoritative target must identify exactly one incoming RL")
    outer = read_sums(sidecars[0])
    if len(outer) != 1:
        raise Failure("outer sidecar must contain exactly one checksum")
    expected_name = safe(outer[0][1]).as_posix()
    if expected_name != Path(expected_name).name:
        raise Failure("outer sidecar must name a top-level ZIP")
    if len(bundles) == 1 and bundles[0].name == expected_name:
        bundle = bundles[0]
        transport = None
    elif not bundles:
        transports = sorted(
            path for path in AUTH.glob("*_BUNDLE_TRANSPORT")
            if path.is_dir() and (path / "PART_SHA256SUMS.txt").is_file()
        )
        if len(transports) != 1:
            raise Failure("expected one physical ZIP or one reconstructible bundle transport")
        bundle = AUTH / expected_name
        transport = transports[0]
    else:
        raise Failure("bundle files are ambiguous or do not match the outer sidecar")
    current_rl = target_numbers.pop()
    completed_candidates = {
        int(match.group(1))
        for path in files
        for match in [re.search(r"RL(\d+)_SESSION_STATE_AND_RL(\d+)_KICKOFF", path.name, re.I)]
        if match and int(match.group(2)) == current_rl
    }
    return {
        "base_head": git("rev-parse", "HEAD").strip(),
        "current_rl": current_rl,
        "handover_generation": next(iter(completed_candidates)) if len(completed_candidates) == 1 else None,
        "target": targets[0].relative_to(ROOT).as_posix(),
        "bundle": bundle.relative_to(ROOT).as_posix(),
        "bundle_transport": transport.relative_to(ROOT).as_posix() if transport else None,
        "outer_sidecar_matches": digest(bundle) == outer[0][0] if bundle.is_file() else None,
        "working_tree_clean": not bool(git("status", "--porcelain", "--untracked-files=all").strip()),
    }


def snapshot():
    entries = []
    for raw in git("ls-files", "-z", "--", "authoritative").split("\0"):
        if raw:
            path = ROOT / raw
            if not path.is_file():
                raise Failure("tracked authoritative file missing: " + raw)
            entries.append({"path": raw, "bytes": path.stat().st_size, "sha256": digest(path)})
    if not entries:
        raise Failure("no tracked authoritative files")
    incoming = state()
    return {"format": "rl-authoritative-snapshot-v1", "base_head": incoming["base_head"],
            "current_rl": incoming["current_rl"], "tree": "authoritative", "entries": sorted(entries, key=lambda x: x["path"])}


def read_sums(path):
    records = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            bits = line.split(maxsplit=1)
            if len(bits) != 2 or not re.fullmatch(r"[0-9a-fA-F]{64}", bits[0]):
                raise Failure("invalid checksum record at %s:%d" % (path, n))
            records.append((bits[0].lower(), bits[1].strip().lstrip("*")))
    if not records:
        raise Failure("empty checksum file: " + str(path))
    return records


def verify_incoming():
    incoming = state()
    bundle = ROOT / incoming["bundle"]
    sidecars = list(AUTH.glob("*.zip.sha256"))
    if len(sidecars) != 1 or sidecars[0].name != bundle.name + ".sha256":
        raise Failure("bundle sidecar is missing or ambiguous")
    outer = read_sums(sidecars[0])
    if len(outer) != 1 or safe(outer[0][1]).as_posix() != bundle.name:
        raise Failure("outer SHA-256 sidecar mismatch")
    with tempfile.TemporaryDirectory(prefix="rl-fresh-") as temp:
        if bundle.is_file():
            checked_bundle = bundle
        else:
            transport = ROOT / (incoming["bundle_transport"] or "")
            records = read_sums(transport / "PART_SHA256SUMS.txt")
            parts = []
            for expected, name in records:
                part = transport / safe(name)
                if not part.is_file() or digest(part) != expected:
                    raise Failure("bundle transport part mismatch: " + name)
                parts.append(part)
            if not parts:
                raise Failure("bundle transport has no parts")
            try:
                raw = base64.b64decode("".join(part.read_text(encoding="utf-8").strip() for part in parts), validate=True)
            except ValueError as error:
                raise Failure("bundle transport Base64 decode failed: %s" % error)
            checked_bundle = Path(temp) / bundle.name
            checked_bundle.write_bytes(raw)
        if digest(checked_bundle) != outer[0][0]:
            raise Failure("outer SHA-256 sidecar mismatch")
        with zipfile.ZipFile(checked_bundle) as archive:
            for name in archive.namelist():
                if name.rstrip("/"):
                    safe(name.rstrip("/"))
            archive.extractall(temp)
        manifests = list(Path(temp).rglob("SHA256SUMS.txt"))
        if len(manifests) != 1:
            raise Failure("fresh unpack needs exactly one SHA256SUMS.txt")
        manifest = manifests[0]
        for expected, name in read_sums(manifest):
            checked = manifest.parent / safe(name.lstrip("./"))
            if not checked.is_file() or digest(checked) != expected:
                raise Failure("internal manifest mismatch: " + name)
        verifiers = sorted((manifest.parent / "verification").glob("verify_*.py"))
        if not verifiers:
            raise Failure("no portable fast verifier in fresh unpack")
        for verifier in verifiers:
            run = subprocess.run([sys.executable, str(verifier)], cwd=manifest.parent, text=True, capture_output=True)
            if run.returncode:
                raise Failure("fresh-unpack verifier failed: %s\n%s" % (verifier.name, (run.stdout + run.stderr).strip()))


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cmd_status(_):
    print(json.dumps(state(), indent=2, sort_keys=True))


def cmd_snapshot(args):
    value = snapshot()
    if args.output:
        output = Path(args.output)
        if not output.is_absolute(): output = ROOT / output
        write_json(output, value)
        print(output)
    else:
        print(json.dumps(value, indent=2, sort_keys=True))


def cmd_check_snapshot(args):
    try:
        old = json.loads(Path(args.snapshot).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise Failure("cannot read snapshot: %s" % error)
    if old != snapshot():
        raise Failure("authoritative snapshot mismatch; do not promote")
    print("authoritative snapshot: PASS")


def cmd_verify(_):
    verify_incoming()
    print("incoming outer sidecar: PASS")
    print("incoming internal manifest: PASS")
    print("incoming fresh-unpack fast verifier suite: PASS")


def cmd_checkpoint(args):
    incoming = state(); rl = args.rl or incoming["current_rl"]
    if not incoming["working_tree_clean"]:
        raise Failure("refuse to initialize a mathematical checkpoint with tracked or untracked repository changes")
    if rl != incoming["current_rl"]:
        raise Failure("checkpoint RL must equal the current incoming RL")
    work = ROOT / ".rl-work" / ("RL%d" % rl)
    if work.exists():
        raise Failure("refuse to overwrite checkpoint: " + str(work))
    work.mkdir(parents=True); (work / "artifacts").mkdir()
    write_json(work / "authoritative-snapshot.json", snapshot())
    write_json(work / "STATE.json", {
        "format": "rl-local-checkpoint-v1", "base_head": incoming["base_head"], "current_rl": rl,
        "authoritative_target": args.target or incoming["target"], "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "last_fully_verified_checkpoint": "Incoming authoritative verification passed; no new mathematics started.",
        "new_results": [], "promoted_exact_certificate_ranges": [], "incomplete_or_unverified_ranges": [],
        "corrections_or_demotions": [], "verifier_runs": [], "failed_or_abandoned_routes": [],
        "next_step": "Read the authoritative target.", "stop_and_repair_active": False})
    (work / "commands.log").write_text("# Append reproducible commands and outcomes here.\n", encoding="utf-8")
    (work / "CHECKPOINT.md").write_text("# Local RL checkpoint (NOT AUTHORITATIVE)\n\n"
        "- BASE_HEAD: `%s`\n- Current incoming RL: `RL%d`\n- Target: `%s`\n"
        "- Last fully verified state: incoming verification passed; no new mathematics started.\n"
        "- New results / exact ranges / unverified work / corrections: none.\n"
        "- Stop-and-repair active: no.\n- Next step: read the target and log verified milestones.\n\n"
        "This ignored directory is a resumability aid, never proof state or a promotion candidate.\n" % (incoming["base_head"], rl, args.target or incoming["target"]), encoding="utf-8")
    print(work)


def cmd_candidate(args):
    candidate = Path(args.candidate).resolve(); path = candidate / "PROMOTION_MANIFEST.json"
    if not path.is_file(): raise Failure("promotion candidate lacks PROMOTION_MANIFEST.json")
    try: manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error: raise Failure("cannot read promotion manifest: %s" % error)
    required = {"format", "current_rl", "next_rl", "completed_session", "next_authoritative", "bundle", "sidecar", "fresh_unpack_report", "verifier_commands", "red_team_report"}
    if not isinstance(manifest, dict) or not required.issubset(manifest) or manifest["format"] != "rl-promotion-candidate-v1":
        raise Failure("promotion manifest is incomplete")
    incoming = state()
    if manifest["current_rl"] != incoming["current_rl"] or manifest["next_rl"] != incoming["current_rl"] + 1:
        raise Failure("promotion manifest has the wrong RL sequence")
    if not isinstance(manifest["verifier_commands"], list) or not manifest["verifier_commands"]:
        raise Failure("promotion candidate must list verifier commands")
    for key in required - {"format", "current_rl", "next_rl", "verifier_commands"}:
        if not isinstance(manifest[key], str) or not (candidate / safe(manifest[key])).exists():
            raise Failure("promotion candidate missing artifact: " + key)
    print("promotion candidate completeness: PASS (mathematical judgement still required)")


def cmd_preflight(args):
    cmd_check_snapshot(argparse.Namespace(snapshot=args.snapshot))
    cmd_candidate(argparse.Namespace(candidate=args.candidate))
    print("preflight: PASS (does not stage, move, or commit files)")


def _authoritative_startup_references():
    entrypoint = AUTH / "START_HERE.md"
    if not entrypoint.is_file():
        raise Failure("authoritative/START_HERE.md is missing")
    text = entrypoint.read_text(encoding="utf-8")
    reads = []
    commands = []
    for token in re.findall(r"`([^`]+)`", text):
        token = token.strip()
        if token.startswith(("python3 ", "bash ")):
            parts = shlex.split(token)
            if len(parts) >= 2:
                script = Path(parts[1])
                candidate = (AUTH / script).resolve()
                try:
                    candidate.relative_to(AUTH.resolve())
                except ValueError:
                    pass
                else:
                    if candidate.is_file():
                        parts[1] = candidate.relative_to(ROOT).as_posix()
                        parts[2:] = ["authoritative" if item == "." else item for item in parts[2:]]
            commands.append(" ".join(shlex.quote(item) for item in parts))
            continue
        candidate = (AUTH / token.lstrip("./")).resolve()
        try:
            candidate.relative_to(AUTH.resolve())
        except ValueError:
            continue
        if candidate.is_file() and candidate.suffix.lower() == ".md":
            reads.append(candidate.relative_to(ROOT).as_posix())
    return sorted(set(reads)), list(dict.fromkeys(commands))


def _authoritative_status_paths():
    ledgers = []
    red_teams = []
    for path in sorted(AUTH.glob("*.md")):
        name = path.name.upper()
        relative = path.relative_to(ROOT).as_posix()
        if "CERTIFIED_FACTS" in name or "PROOF_LEDGER" in name or (
            ("CORRECTION" in name or "DEMOTION" in name) and "LEDGER" in name
        ):
            ledgers.append(relative)
        if "RED_TEAM" in name:
            red_teams.append(relative)
    return ledgers, red_teams


def _index_summary():
    path = ROOT / "knowledge" / "index_metadata.json"
    if not path.is_file():
        return {"present": False, "validation_command": "python3 tools/rl_conveyor.py index-validate"}
    try:
        metadata = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise Failure("knowledge/index_metadata.json is invalid: %s" % error)
    return {
        "present": True,
        "format": metadata.get("format"),
        "container_count": metadata.get("container_count"),
        "generation_record_count": metadata.get("generation_record_count"),
        "result_record_count": metadata.get("result_record_count"),
        "validation_command": "python3 tools/rl_conveyor.py index-validate",
    }


def startup_state():
    incoming = state()
    current_reads, current_commands = _authoritative_startup_references()
    status_paths, red_team_paths = _authoritative_status_paths()
    read_order = list(dict.fromkeys([
        "AGENTS.md",
        "START_HERE.md",
        "authoritative/START_HERE.md",
        *status_paths,
        *red_team_paths,
        *current_reads,
    ]))
    return {
        "incoming_rl": incoming["current_rl"],
        "handover_generation": incoming["handover_generation"],
        "target": incoming["target"],
        "bundle": incoming["bundle"],
        "incoming_outer_sidecar_matches": incoming["outer_sidecar_matches"],
        "minimal_read_order": read_order,
        "current_status_paths": status_paths,
        "required_red_team_paths": red_team_paths,
        "required_commands": [
            "python3 tools/rl_conveyor.py status",
            "python3 tools/rl_conveyor.py verify-incoming",
            *current_commands,
        ],
        "history_queries": [
            "python3 tools/rl_conveyor.py session RL<N>",
            "python3 tools/rl_conveyor.py result '<name or alias>'",
        ],
        "normally_excluded_search_surfaces": [
            "sessions/", "Archive/", "ZIP contents", "bundle transports",
            "generated bundle copies", "certificate payloads",
        ],
        "knowledge_index": _index_summary(),
    }


def cmd_startup(args):
    value = startup_state()
    if args.json:
        print(json.dumps(value, indent=2, sort_keys=True))
        return
    print("Incoming: RL%d" % value["incoming_rl"])
    if value["handover_generation"] is not None:
        print("Handover generation: RL%d" % value["handover_generation"])
    print("Target: %s" % value["target"])
    print("Minimal read order:")
    for path in value["minimal_read_order"]:
        print("  " + path)
    print("Required commands:")
    for command in value["required_commands"]:
        print("  " + command)
    print("History is query-only by default: session RL<N> / result <name-or-alias>")
    print("Do not recursively search sessions/, Archive/, bundles, or certificate payloads during normal startup.")


def _first_paths(record, key, limit=3):
    return record.get(key, [])[:limit]


def _print_generation(record, role):
    print("%s: %s" % (role, record["generation_id"]))
    for path in record.get("generation_paths", []):
        print("  root: " + path)
    labels = (
        ("report", "main_report_paths"),
        ("state", "session_state_handover_paths"),
        ("target", "target_paths"),
        ("proof ledger", "proof_ledger_paths"),
        ("correction ledger", "correction_demotion_ledger_paths"),
        ("verifier", "verifier_paths"),
        ("certificate root", "certificate_roots"),
        ("bundle", "bundle_paths"),
    )
    for label, key in labels:
        for path in _first_paths(record, key):
            print("  %s: %s" % (label, path))
    for warning in record.get("ambiguities", []):
        print("  ambiguity: " + warning)


def cmd_session(args):
    try:
        rl = parse_rl_identifier(args.rl)
        value = query_sessions(ROOT, rl)
    except CatalogError as error:
        raise Failure(str(error)) from error
    if args.json:
        print(json.dumps(value, indent=2, sort_keys=True))
        return
    print("Historical locator: RL%d" % rl)
    seen = set()
    for role, key in (
        ("completed generation", "completed_generation_records"),
        ("incoming handover", "incoming_generation_records"),
        ("container label", "container_label_records"),
        ("embedded historical locator", "embedded_locator_records"),
    ):
        for record in value[key]:
            identity = (record["generation_id"], tuple(record["generation_paths"]))
            if identity in seen:
                continue
            seen.add(identity)
            _print_generation(record, role)
    if not seen:
        print("No explicit indexed record. Use an exceptional targeted audit; do not infer from a missing container label.")
    print(value["note"])


def cmd_result(args):
    try:
        value = query_results(ROOT, args.query, args.limit)
    except CatalogError as error:
        raise Failure(str(error)) from error
    if args.json:
        print(json.dumps(value, indent=2, sort_keys=True))
        return
    print("Result locator: %s (%d matches)" % (args.query, value["match_count"]))
    for record in value["matches"]:
        name = record.get("name") or "unnamed recorded entry"
        status = record.get("recorded_classification") or "classification not explicitly encoded"
        print("- %s [%s]" % (name, status))
        print("  %s:%d" % (record["source_path"], record["source_line_start"]))
        print("  source: %s; generation: %s" % (record["source_kind"], record.get("generation_id") or "unknown"))
        if record["is_correction_or_demotion_record"]:
            print("  correction/demotion pointer: yes")
        for path in record.get("verifier_paths", [])[:2]:
            print("  session verifier candidate (not asserted claim-specific): " + path)
        for path in record.get("certificate_roots", [])[:2]:
            print("  session certificate root (not asserted claim-specific): " + path)
    if not value["matches"]:
        print("No conservative indexed match. Use a targeted source audit only if a live dependency requires it.")
    if value["review_marker"]:
        print(value["review_marker"])
    if value["preferred_full_provenance_source"]:
        print("Preferred full-provenance source: " + value["preferred_full_provenance_source"])
    print(value["status_policy"])


def cmd_index_build(args):
    try:
        metadata = write_indexes(ROOT)
    except CatalogError as error:
        raise Failure(str(error)) from error
    if args.json:
        print(json.dumps(metadata, indent=2, sort_keys=True))
    else:
        print(
            "knowledge index: BUILT (%d containers, %d generation locators, %d result locators)"
            % (metadata["container_count"], metadata["generation_record_count"], metadata["result_record_count"])
        )


def cmd_index_validate(args):
    try:
        result = validate_indexes(ROOT)
    except CatalogError as error:
        raise Failure(str(error)) from error
    if not result["current"]:
        details = ", ".join(item["path"] + " (" + item["reason"] + ")" for item in result["mismatches"])
        raise Failure("knowledge index is stale: " + details)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(
            "knowledge index: PASS (%d containers, %d generation locators, %d result locators; unlocated labels: %s)"
            % (
                result["container_count"], result["generation_record_count"], result["result_record_count"],
                ", ".join("RL%d" % number for number in result["unlocated_rls"]) or "none",
            )
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__); sub = parser.add_subparsers(required=True)
    sub.add_parser("status").set_defaults(func=cmd_status)
    p = sub.add_parser("snapshot"); p.add_argument("--output"); p.set_defaults(func=cmd_snapshot)
    p = sub.add_parser("check-snapshot"); p.add_argument("snapshot"); p.set_defaults(func=cmd_check_snapshot)
    sub.add_parser("verify-incoming").set_defaults(func=cmd_verify)
    p = sub.add_parser("init-checkpoint"); p.add_argument("--rl", type=int); p.add_argument("--target"); p.set_defaults(func=cmd_checkpoint)
    p = sub.add_parser("check-promotion"); p.add_argument("candidate"); p.set_defaults(func=cmd_candidate)
    p = sub.add_parser("preflight"); p.add_argument("snapshot"); p.add_argument("candidate"); p.set_defaults(func=cmd_preflight)
    p = sub.add_parser("startup"); p.add_argument("--json", action="store_true"); p.set_defaults(func=cmd_startup)
    p = sub.add_parser("session"); p.add_argument("rl"); p.add_argument("--json", action="store_true"); p.set_defaults(func=cmd_session)
    p = sub.add_parser("result"); p.add_argument("query"); p.add_argument("--limit", type=int, default=20); p.add_argument("--json", action="store_true"); p.set_defaults(func=cmd_result)
    p = sub.add_parser("index-build"); p.add_argument("--json", action="store_true"); p.set_defaults(func=cmd_index_build)
    p = sub.add_parser("index-validate"); p.add_argument("--json", action="store_true"); p.set_defaults(func=cmd_index_validate)
    try: args = parser.parse_args(); args.func(args)
    except Failure as error:
        print("FAIL CLOSED: " + str(error), file=sys.stderr); return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
