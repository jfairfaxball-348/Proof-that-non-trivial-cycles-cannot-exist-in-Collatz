from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('zero36_core.py')))['verify'](30, 36)
