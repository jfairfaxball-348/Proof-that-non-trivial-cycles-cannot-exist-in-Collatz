from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('zero37_core.py')))['verify'](24, 37)
