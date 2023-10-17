from os import system, cpu_count
from pathlib import Path
import shutil

PYTHON_DIR_PATH = Path(__file__).parent.resolve()
PROJECT_DIR_PATH = PYTHON_DIR_PATH.parent

FETCH_DIR_NAME = "fetch"
FETCH_DIR_PATH = PROJECT_DIR_PATH / FETCH_DIR_NAME

EXTERNAL_DIR_NAME = "external"
EXTERNAL_DIR_PATH = PROJECT_DIR_PATH / EXTERNAL_DIR_NAME

BUILD_DIR_NAME = "build"
BUILD_DIR_PATH = PROJECT_DIR_PATH / BUILD_DIR_NAME

INCLUDE_DIR_NAME = "include"
LIB_DIR_NAME = "lib"

CPU_COUNT = cpu_count()
