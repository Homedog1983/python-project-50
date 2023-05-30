import pytest
from gendiff.file_parser import get_dict_from_file
from tests.test_generate_diff import get_paths


@pytest.mark.parametrize("name, name_expected", [
    ('file1.json', 'dict_1.txt'),
    ('file2.json', 'dict_2.txt'),
    ('file1.yml', 'dict_1.txt'),
    ('file2.yml', 'dict_2.txt'),
    ('file1.yaml', 'dict_1.txt'),
    ('file2.yaml', 'dict_2.txt'),
    ('file2.yml', 'dict_2.txt'),
    ('file1.yaml', 'dict_1.txt'),
    ('wrong_type.txt', 'dict_empty.txt'),
    ('f.json', 'dict_empty.txt')
])
def test_get_dict_from_file(name, name_expected):
    path, path_expected = get_paths(name, name_expected)
    with open(path_expected) as file_expected:
        content_expected = eval(file_expected.read())
        assert get_dict_from_file(path) == content_expected
