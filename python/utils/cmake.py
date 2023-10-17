from python.globals import BUILD_DIR_PATH, PROJECT_DIR_PATH
from python.utils import system

from enum import Enum, auto

class BuildType(Enum):
    DEBUG = auto()
    RELEASE = auto()


def configure(build_dir_path):
    cmd_list = _config_command(build_dir_path)
    system.run(cmd_list)


def _config_command(
    build_dir_path=BUILD_DIR_PATH,
    cmake_source_dir=PROJECT_DIR_PATH,
    export_compile_command=True,
    build_type=BuildType.DEBUG,
):
    cmd_list = []
    
    cmd_list.append("cmake")
    
    if export_compile_command:
        cmd_list.append("-DCMAKE_EXPORT_COMPILE_COMMANDS=ON")

    if build_type == BuildType.DEBUG:
        cmd_list.append("-DCMAKE_BUILD_TYPE=Debug")
    elif build_type == BuildType.RELEASE:
        cmd_list.append("-DCMAKE_BUILD_TYPE=Release")
    
    cmd_list.append(f"-S{cmake_source_dir}")
    cmd_list.append(f"-B{build_dir_path}")
    
    return cmd_list


def build(build_dir_path):
    cmd_list = _build_command(build_dir_path)
    print(f">> {' '.join(cmd_list)}")
    system.run(cmd_list)


def _build_command(
    build_dir_path=BUILD_DIR_PATH,
):
    cmd_list = []
    cmd_list.append("cmake")
    cmd_list.append("--build")
    cmd_list.append(f"{build_dir_path}")
    return cmd_list
