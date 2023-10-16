from pathlib import Path

PYTHON_DIR_PATH = Path(__file__).parent.resolve()
PROJECT_DIR_PATH = PYTHON_DIR_PATH.parent

EXTERNAL_DIR_NAME = "external"
EXTERNAL_DIR_PATH = PROJECT_DIR_PATH / EXTERNAL_DIR_NAME

BUILD_DIR_NAME = "build"
BUILD_DIR_PATH = PROJECT_DIR_PATH / BUILD_DIR_NAME