#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "RL309_REPORT.md",
    "RL309_DEPENDENCY_MAP.md",
    "RL309_LEVERAGE_AUDIT.md",
    "RL309_REPOSITORY_MECHANICS_AUDIT.md",
    "RL309_RED_TEAM.md",
    "RL309_CLOSEOUT.md",
    "RL309_INCOMING_TARGET.md",
    "RL309_LOSSLESS_TRANSPORT_NOTE.md",
    "RL310_UNIVERSAL_FULL_D_OWNERSHIP_COERCIVITY_GLOBAL_EXTRACTION_TARGET.md",
]
for rel in required:
    p = ROOT / rel
    assert p.is_file(), f"missing {rel}"

report = (ROOT / "RL309_REPORT.md").read_text()
dep = (ROOT / "RL309_DEPENDENCY_MAP.md").read_text()
red = (ROOT / "RL309_RED_TEAM.md").read_text()
close = (ROOT / "RL309_CLOSEOUT.md").read_text()
target = (ROOT / "RL310_UNIVERSAL_FULL_D_OWNERSHIP_COERCIVITY_GLOBAL_EXTRACTION_TARGET.md").read_text()

checks = [
    ("no new theorem", "new_mathematical_theorems=0" in close),
    ("Gate A open", "gate_a_global=open" in close),
    ("Gate B open", "gate_b_global=open" in close),
    ("global exclusion open", "global_nontrivial_cycle_exclusion=open" in close),
    ("primary architecture", "universal full-D ownership coercivity/extraction" in report),
    ("dependency primary open", "PRIMARY GLOBAL ARROW" in dep),
    ("quotient interface", "ordinary affine `+1` update" in dep),
    ("red team pass", "RL309_ROADMAP_RED_TEAM_PASS" in red),
    ("RL310 all-scale", "uniform all-scale owned coercivity/extraction theorem" in target),
    ("parent delta", "PARENT_DIFFICULTY_DELTA" in target),
    ("catalogue deferred", "stale/deferred" in close),
]
for name, ok in checks:
    assert ok, f"failed check: {name}"

manifest = ROOT / "SHA256SUMS.txt"
if manifest.exists():
    for line in manifest.read_text().splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        p = ROOT / rel
        assert p.is_file(), f"manifest missing {rel}"
        got = hashlib.sha256(p.read_bytes()).hexdigest()
        assert got == digest, f"hash mismatch {rel}"

print("RL309_CLOSEOUT_VERIFIER_GREEN")
