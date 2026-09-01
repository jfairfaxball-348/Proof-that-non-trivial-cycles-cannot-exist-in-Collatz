#!/usr/bin/env python3
"""Run the exact RL223 bounded fixed-count residue certificate verifier."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "support" / "verify_rl223_bounded_probe_core.py"
CERTIFICATE = ROOT / "certificates" / "rl223_bounded_residue_probe.json"


def main() -> None:
    run = subprocess.run(
        [sys.executable, str(CORE), str(CERTIFICATE)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if run.returncode:
        raise SystemExit((run.stdout + run.stderr).strip())
    expected = (
        "PASS q=5..1023 eligible=340 surjective=340 "
        "max_minimal_h=16 scope=UNCONSTRAINED_BINARY_WORDS_ONLY"
    )
    output = run.stdout.strip()
    assert output == expected, output
    print("RL223 BOUNDED COUNT-ONLY RESIDUE PROBE: PASS")
    print(output)


if __name__ == "__main__":
    main()
