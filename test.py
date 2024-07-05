from subprocess import run
from pathlib import Path
import venv

root = Path(__file__).parent

[wheel_file] = (root / "dist").glob("*.whl")

venv_dir = root / "venv"
venv.create(str(venv_dir), clear=True, with_pip=True, symlinks=True)

pip = str(venv_dir / "bin" / "pip")
run([pip, "install", str(wheel_file)], check=True)

python = str(venv_dir / "bin" / "python")
script = """\
import sys
sys.exit("coverage" not in sys.modules)
"""
run([python, "-c", script], check=True)
