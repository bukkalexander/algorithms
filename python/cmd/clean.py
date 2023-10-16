import shutil
from python.globals import EXTERNAL_DIR_PATH, BUILD_DIR_PATH


GENERATED_DIR_PATH_LIST = [
    EXTERNAL_DIR_PATH,
    BUILD_DIR_PATH,
]


def clean(args):
    _clean(GENERATED_DIR_PATH_LIST)


def _clean(dir_path_list):
    for dir_path in dir_path_list:
        _remove(dir_path)


def _remove(path):
    if not path.exists():
        return
    if path.is_dir:
        shutil.rmtree(path)
    else:
        path.unlink()
    print(f"removed: {path}")