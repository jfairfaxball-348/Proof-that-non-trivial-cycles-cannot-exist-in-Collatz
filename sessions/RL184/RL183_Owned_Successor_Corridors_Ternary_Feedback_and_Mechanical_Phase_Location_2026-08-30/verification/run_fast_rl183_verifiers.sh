#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_rl183_owned_successor_corridors.py
