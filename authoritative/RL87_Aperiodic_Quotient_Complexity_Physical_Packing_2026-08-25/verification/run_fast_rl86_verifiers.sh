#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python verification/verify_rl86_roof_feeder_ray.py
