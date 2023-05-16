import pytest
from gendiff.file_parser import get_dict_from_file


@pytest.fixture
def paths():
    paths = {
          'json1': 'tests/fixtures/file1.json',
          'json2': 'tests/fixtures/file2.json',
          'yml1': 'tests/fixtures/file1.yml',
          'yml2': 'tests/fixtures/file2.yml',
          'yaml2': 'tests/fixtures/file2.yaml',
          'not_exist': 'tests/fixtures/f.json',
          'wrong_type': 'tests/fixtures/wrong_type.txt'
          }
    return paths


@pytest.fixture
def expected_dicts():
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
    return {'1': dict1, '2': dict2, 'empty': {}}


def test_get_dict_from_file(paths, expected_dicts) -> dict:
    result = get_dict_from_file(paths['json1'])
    assert result == expected_dicts['1']
    result = get_dict_from_file(paths['yaml2'])
    assert result == expected_dicts['2']
    result = get_dict_from_file(paths['json2'])
    assert result == expected_dicts['2']
    result = get_dict_from_file(paths['yaml2'])
    assert result == expected_dicts['2']
    result = get_dict_from_file(paths['yml2'])
    assert result == expected_dicts['2']
    result = get_dict_from_file(paths['wrong_type'])
    assert result == expected_dicts['empty']
    result = get_dict_from_file(paths['not_exist'])
    assert result == expected_dicts['empty']
