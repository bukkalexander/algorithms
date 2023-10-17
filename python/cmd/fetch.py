from python.dependency.googletest import GoogleTestDependency
from python.utils import system
from python.globals import EXTERNAL_DIR_PATH, FETCH_DIR_PATH


def fetch(args):
    print("> fetch")
    _fetch()


def _fetch():
    system.remove(FETCH_DIR_PATH)
    system.remove(EXTERNAL_DIR_PATH)
    EXTERNAL_DIR_PATH.mkdir()
    FETCH_DIR_PATH.mkdir()
    google_test_dependency = GoogleTestDependency()
    google_test_dependency.setup()
    system.remove(FETCH_DIR_PATH)

