from subprocess import run
from tempfile import mkdtemp
from pathlib import Path
from shutil import copyfile, rmtree

root = Path(__file__).parent
build_dir = root / "build"
build_dir.mkdir(exist_ok=True)
work_dir = Path(mkdtemp(prefix="wheel-", dir=build_dir))


# Generate an empty wheel with the metadata from pyproject.toml.
run(
    [
        "python3",
        "-m",
        "pip",
        "wheel",
        "--no-deps",
        "--wheel-dir",
        str(work_dir),
        str(root),
    ],
    check=True,
)
[wheel_file] = work_dir.glob("*.whl")
print(f"Generated {wheel_file}")

# Unpack the wheel so we can modify it.
run(["python3", "-m", "wheel", "unpack", str(wheel_file)], cwd=work_dir, check=True)
wheel_file.unlink()
[wheel_dir] = work_dir.iterdir()
print(f"Unpacked to {wheel_dir}")

# Inject the _coverage.pth file. This is a purelib wheel so it'll get dropped in
# site-packages when pip installs the wheel.
copyfile(
    root / "src" / "_coverage.pth",
    wheel_dir / "_coverage.pth",
)

# Repack the wheel.
run(["python3", "-m", "wheel", "pack", str(wheel_dir)], cwd=work_dir, check=True)
dist_dir = root / "dist"
dist_dir.mkdir(exist_ok=True)
copyfile(wheel_file, dist_dir / wheel_file.name)
print(f"Built {wheel_file.stem}")

# Cleanup
rmtree(work_dir)
