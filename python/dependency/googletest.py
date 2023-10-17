import shutil
from python.dependency.dependency import Dependency
from python.globals import BUILD_DIR_NAME, CPU_COUNT, EXTERNAL_DIR_PATH, FETCH_DIR_PATH, INCLUDE_DIR_NAME, LIB_DIR_NAME
from python.utils import system


class GoogleTestDependency(Dependency):
    def __init__(self):
        self.name = "googletest"

        self.repo_dir_name = self.name
        self.repo_dir_path = FETCH_DIR_PATH / self.repo_dir_name
        self.url = "https://github.com/google/googletest.git"
        self.branch = "v1.14.0"

        self.build_dir_path = self.repo_dir_path / BUILD_DIR_NAME

        self.google_test_module_name = self.name
        self.google_test_include_dir_path = self.repo_dir_path / self.google_test_module_name / INCLUDE_DIR_NAME

        self.google_mock_module_name = "googlemock"
        self.google_mock_include_dir_path = self.repo_dir_path / self.google_mock_module_name / INCLUDE_DIR_NAME

        self.lib_dir_path = self.build_dir_path / LIB_DIR_NAME

        self.install_dir_path = EXTERNAL_DIR_PATH / self.name
        self.install_include_dir_path = self.install_dir_path / INCLUDE_DIR_NAME
        self.install_lib_dir_path = self.install_dir_path / LIB_DIR_NAME
        

        super().__init__()
    
    def fetch(self):
        print(f"clone repo {self.url}")
        cmd_list = []
        cmd_list.append("git")
        cmd_list.append("clone")
        cmd_list.append(self.url)
        if self.branch:
            cmd_list.append("-b")
            cmd_list.append(self.branch)
        system.run(cmd_list, cwd=self.repo_dir_path.parent)
    
    def build(self):
        print(f"build '{self.name}'")
        self.build_dir_path.mkdir()
        system.run(["cmake", ".."], cwd=self.build_dir_path)
        system.run(["make", f"-j{CPU_COUNT}"], cwd=self.build_dir_path)
    
    def install(self):
        self.install_dir_path.mkdir()
        
        self.install_include_dir_path.mkdir()
        shutil.copytree(self.google_test_include_dir_path, self.install_include_dir_path, dirs_exist_ok=True)
        shutil.copytree(self.google_mock_include_dir_path, self.install_include_dir_path, dirs_exist_ok=True)
        
        self.install_lib_dir_path.mkdir()
        shutil.copytree(self.lib_dir_path, self.install_lib_dir_path, dirs_exist_ok=True)
