#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 verification/inherited_rl63/verify_rl62_rl59_terminal_potential_sign.py > /tmp/rl64_sign.out
diff -u verification/inherited_rl63/RL62_RL59_TERMINAL_POTENTIAL_SIGN_AUDIT.out /tmp/rl64_sign.out
python3 verification/inherited_rl63/verify_rl63_even_exit_selector.py > /tmp/rl64_rl63_selector.out
diff -u verification/inherited_rl63/RL63_EVEN_EXIT_SELECTOR.out /tmp/rl64_rl63_selector.out
python3 historical/RL47_verify_rl47_phase_coordinate.py > /tmp/rl64_historical_phase.out
grep -q '^RL47 phase-coordinate verifier: PASS$' /tmp/rl64_historical_phase.out
python3 verification/verify_rl64_all_word_cylinders.py > /tmp/rl64_selector.out
grep -q '^RL64 all-word cylinder verifier: PASS$' /tmp/rl64_selector.out
echo 'FAST_RL64_VERIFIERS PASS'
