import pytest
from gendiff.file_parser import get_dict_from_file


def params():
    paths = {
        'json1': 'tests/fixtures/file1.json',
        'json2': 'tests/fixtures/file2.json',
        'yml1': 'tests/fixtures/file1.yml',
        'yml2': 'tests/fixtures/file2.yml',
        'yaml1': 'tests/fixtures/file1.yaml',
        'yaml2': 'tests/fixtures/file2.yaml',
        'not_exist': 'tests/fixtures/f.json',
        'wrong_type': 'tests/fixtures/wrong_type.txt'
    }

    dict1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    dict2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }
    dicts = {'1': dict1, '2': dict2, 'empty': {}}

    return [
        (paths['json1'], dicts['1']),
        (paths['json2'], dicts['2']),
        (paths['yml1'], dicts['1']),
        (paths['yml2'], dicts['2']),
        (paths['yaml1'], dicts['1']),
        (paths['yaml2'], dicts['2']),
        (paths['yml2'], dicts['2']),
        (paths['yaml1'], dicts['1']),
        (paths['wrong_type'], dicts['empty']),
        (paths['not_exist'], dicts['empty'])
    ]


@pytest.mark.parametrize("path, expected_dict", params())
def test_get_dict_from_file(path, expected_dict):
    assert get_dict_from_file(path) == expected_dict
