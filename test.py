"""
Installing `coverage.pth` causes `coverage.process_startup()` to be called
when Python starts.
"""

import os
from subprocess import run
from pathlib import Path
import venv

root = Path(__file__).parent

[wheel_file] = (root / "dist").glob("*.whl")

venv_dir = root / "venv"
venv.create(str(venv_dir), clear=True, with_pip=True, symlinks=True)

pip = str(venv_dir / "bin" / "pip")
run([pip, "install", "-r", "requirements_test.txt", str(wheel_file)], check=True)

python = str(venv_dir / "bin" / "python")
script = """\
import sys
if "coverage" not in sys.modules:
    print("coverage hasn't been imported")
    sys.exit(1)
import coverage
if not hasattr(coverage.process_startup, "coverage"):
    print("coverage.process_startup() wasn't called (or the implementation changed)")
    sys.exit(1)
print("OK!")
"""
run(
    [python, "-c", script],
    env={**os.environ, "COVERAGE_PROCESS_START": "/dev/null"},
    check=True,
)
