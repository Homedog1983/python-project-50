import pytest
from gendiff.file_parser import get_dict_from_file


@pytest.mark.parametrize("path, expected_dict", [
    ('file1.json', 'dict_1'),
    ('file2.json', 'dict_2'),
    ('file1.yml', 'dict_1'),
    ('file2.yml', 'dict_2'),
    ('file1.yaml', 'dict_1'),
    ('file2.yaml', 'dict_2'),
    ('file2.yml', 'dict_2'),
    ('file1.yaml', 'dict_1'),
    ('wrong_type.txt', 'empty'),
    ('f.json', 'empty')
])
def test_get_dict_from_file(path, expected_dict):
    full_path = f'tests/fixtures/{path}'
    if expected_dict == 'dict_1':
        expected = {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        }
    elif expected_dict == 'dict_2':
        expected = {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        }
    else:
        expected = {}
    assert get_dict_from_file(full_path) == expected
