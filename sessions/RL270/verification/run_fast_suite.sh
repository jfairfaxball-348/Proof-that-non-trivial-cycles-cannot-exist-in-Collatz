#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_rl270_certificate.py | tee /tmp/rl270_certificate.out
grep -q RL270_CERTIFICATE_PASS /tmp/rl270_certificate.out
python3 redteam_rl270_small.py | tee /tmp/rl270_redteam.out
grep -q RL270_REDTEAM_PASS /tmp/rl270_redteam.out
echo RL270_FAST_SUITE_PASS
