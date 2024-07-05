import os
from subprocess import run
import shlex
from tempfile import mkdtemp
from pathlib import Path
from shutil import copyfile, rmtree


def cmd(*argv, cwd=None):
    print(f"\nRunning {' '.join(shlex.quote(c) for c in argv)} in {cwd or os.getcwd()}")
    return run(argv, cwd=cwd, check=True)


root = Path(__file__).parent
build_dir = root / "build"
build_dir.mkdir(exist_ok=True)
work_dir = Path(mkdtemp(prefix="wheel-", dir=build_dir))


# Generate an empty wheel with the metadata from pyproject.toml.
cmd(
    "python3",
    "-m",
    "pip",
    "wheel",
    "--no-deps",
    "--wheel-dir",
    str(work_dir),
    str(root),
)
[wheel_file] = work_dir.glob("*.whl")
print(f"Generated {wheel_file}")

# Unpack the wheel so we can modify it.
cmd("python3", "-m", "wheel", "unpack", wheel_file.name, cwd=work_dir)
wheel_file.unlink()
[wheel_dir] = work_dir.iterdir()

# Inject the _coverage.pth file. This is a purelib wheel so it'll get dropped in
# site-packages when pip installs the wheel.
copyfile(
    root / "src" / "_coverage.pth",
    wheel_dir / "_coverage.pth",
)

# Repack the wheel.
cmd("python3", "-m", "wheel", "pack", wheel_dir.name, cwd=work_dir)
dist_dir = root / "dist"
dist_dir.mkdir(exist_ok=True)
copyfile(wheel_file, dist_dir / wheel_file.name)
print(f"Built {wheel_file.stem}")

# Cleanup
rmtree(work_dir)
