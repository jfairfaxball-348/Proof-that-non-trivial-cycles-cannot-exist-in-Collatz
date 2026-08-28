#!/usr/bin/env python3
"""Fail-closed, non-promoting utilities for the RL research conveyor."""

import argparse
import base64
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
AUTH = ROOT / "authoritative"


class Failure(RuntimeError):
    pass


def git(*args):
    run = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True)
    if run.returncode:
        raise Failure(run.stderr.strip() or "git command failed")
    return run.stdout


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def safe(name):
    path = PurePosixPath(name)
    if not name or path.is_absolute() or ".." in path.parts:
        raise Failure("unsafe bundle/manifest path: %r" % name)
    return Path(*path.parts)


def state():
    if not AUTH.is_dir():
        raise Failure("authoritative/ is missing")
    files = [p for p in AUTH.rglob("*") if p.is_file()]
    numbers = [int(m.group(1)) for p in files for m in re.finditer(r"RL(\d+)", p.name, re.I)]
    # Authoritative handovers are extracted below one package directory; the
    # target is therefore nested rather than a top-level authority file.
    targets = sorted(AUTH.rglob("*TARGET*.md"))
    bundles = sorted(AUTH.glob("*.zip"))
    sidecars = sorted(AUTH.glob("*.zip.sha256"))
    if not numbers or len(targets) != 1 or len(sidecars) != 1:
        raise Failure("expected one target, one bundle sidecar, and an RL number in authoritative/")
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
    return {
        "base_head": git("rev-parse", "HEAD").strip(),
        "current_rl": max(numbers),
        "target": targets[0].relative_to(ROOT).as_posix(),
        "bundle": bundle.relative_to(ROOT).as_posix(),
        "bundle_transport": transport.relative_to(ROOT).as_posix() if transport else None,
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


def main():
    parser = argparse.ArgumentParser(description=__doc__); sub = parser.add_subparsers(required=True)
    sub.add_parser("status").set_defaults(func=cmd_status)
    p = sub.add_parser("snapshot"); p.add_argument("--output"); p.set_defaults(func=cmd_snapshot)
    p = sub.add_parser("check-snapshot"); p.add_argument("snapshot"); p.set_defaults(func=cmd_check_snapshot)
    sub.add_parser("verify-incoming").set_defaults(func=cmd_verify)
    p = sub.add_parser("init-checkpoint"); p.add_argument("--rl", type=int); p.add_argument("--target"); p.set_defaults(func=cmd_checkpoint)
    p = sub.add_parser("check-promotion"); p.add_argument("candidate"); p.set_defaults(func=cmd_candidate)
    p = sub.add_parser("preflight"); p.add_argument("snapshot"); p.add_argument("candidate"); p.set_defaults(func=cmd_preflight)
    try: args = parser.parse_args(); args.func(args)
    except Failure as error:
        print("FAIL CLOSED: " + str(error), file=sys.stderr); return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
