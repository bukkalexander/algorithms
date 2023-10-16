import pytest

from python.cmd.clean import _clean

@pytest.fixture
def tmp_path_list(tmp_path):
    path_list = []
    
    dir_with_subdir_dir_name = "dir_with_subdir"
    dir_name = "dir"
    dir_path_list = [
        tmp_path / dir_with_subdir_dir_name,
        tmp_path / dir_name,
    ]
    for dir_path in dir_path_list:
        dir_path.mkdir()
    
    subdir_name = "subdir"
    (dir_path_list[0] / subdir_name).mkdir()
    path_list.extend(dir_path_list)
    
    fake_file_name = "fake.txt"
    fake_file_path = tmp_path / fake_file_name
    path_list.append(fake_file_path)
    
    return path_list


def test_clean(tmp_path_list):
    _clean(tmp_path_list)
    for path in tmp_path_list:
        assert not path.exists()