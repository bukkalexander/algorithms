from python.utils import system
from python.globals import BUILD_DIR_PATH
from python.utils import cmake


def build(args):
    print("> build")
    _build(BUILD_DIR_PATH)


def _build(build_dir_path):
    system.remove(build_dir_path)
    build_dir_path.mkdir()
    cmake.configure(build_dir_path)
    cmake.build(build_dir_path)
