#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_rl62_rl59_terminal_potential_sign.py > /tmp/rl63_sign.out
diff -u RL62_RL59_TERMINAL_POTENTIAL_SIGN_AUDIT.out /tmp/rl63_sign.out
python3 verify_rl63_even_exit_selector.py > /tmp/rl63_selector.out
diff -u RL63_EVEN_EXIT_SELECTOR.out /tmp/rl63_selector.out
echo 'FAST_RL63_VERIFIERS PASS'
