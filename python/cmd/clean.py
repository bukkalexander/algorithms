from python.utils import system
from python.globals import EXTERNAL_DIR_PATH, BUILD_DIR_PATH


GENERATED_DIR_PATH_LIST = [
    EXTERNAL_DIR_PATH,
    BUILD_DIR_PATH,
]


def clean(args):
    print("> clean")
    _clean(GENERATED_DIR_PATH_LIST)


def _clean(dir_path_list):
    for dir_path in dir_path_list:
        system.remove(dir_path)
