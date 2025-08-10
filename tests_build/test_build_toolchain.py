import importlib.util
from pathlib import Path


spec = importlib.util.spec_from_file_location(
    "build_module",
    Path(__file__).resolve().parents[1] / "build.py",
)
assert spec and spec.loader
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


def test_accepts_explicit_version():
    assert build._is_valid_toolchain("1.87.0")


def test_rejects_invalid_toolchain():
    assert not build._is_valid_toolchain("beta")
