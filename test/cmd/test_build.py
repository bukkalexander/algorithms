import pytest

from python.cmd.build import _build

@pytest.fixture
def build_dir_path(tmp_path):
    build_dir_name = "build"
    build_dir_path = tmp_path / build_dir_name
    return build_dir_path


def test_build(build_dir_path):
    _build(build_dir_path)