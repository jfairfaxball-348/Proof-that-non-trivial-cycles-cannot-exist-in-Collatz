#!/usr/bin/env python3
from pathlib import Path
import runpy
HERE=Path(__file__).resolve().parent.parent
runpy.run_path(str(HERE/'support'/'verify_rl225_e4_transfer_core.py'), run_name='__main__')
