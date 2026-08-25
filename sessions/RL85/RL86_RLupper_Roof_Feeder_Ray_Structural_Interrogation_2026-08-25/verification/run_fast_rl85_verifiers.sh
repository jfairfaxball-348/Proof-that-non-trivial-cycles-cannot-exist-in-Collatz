#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python verification/verify_rl85_comparative_bridge.py
