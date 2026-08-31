#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 verification/verify_rl201_log_support_repair.py
python3 verification/verify_rl201_successor_corridor.py
python3 verification/verify_rl201_endpoint_moment.py
python3 verification/verify_rl201_coupled_reverse.py
