import pytest
from gendiff.diffs.flat_jsons_diff import converted_to_json_str
from gendiff.diffs.flat_jsons_diff import get_dict_from_json
from gendiff.diffs.flat_jsons_diff import get_flat_jsons_diff
from tests.fixtures import flat_jsons_diff_test_data as data

JSON_PATH1 = 'tests/fixtures/file1.json'
JSON_PATH2 = 'tests/fixtures/file2.json'
WRONG_PATH = 'tests/fixtures/f.json'
JSON_WRONG_TYPE_PATH = 'tests/fixtures/wrong_type.txt'
DIFF12_PATH = 'tests/fixtures/flat_jsons_diff12.txt'
DIFF21_PATH = 'tests/fixtures/flat_jsons_diff21.txt'


@pytest.fixture
def dict1() -> dict:
    return data.dict1


@pytest.fixture
def dict2() -> dict:
    return data.dict2


@pytest.fixture
def diff12():
    ls = []
    with open(DIFF12_PATH, 'r') as file_obj:
        for line in file_obj:
            ls.append(line)
    return ''.join(ls)[:-1]


@pytest.fixture
def diff21():
    ls = []
    with open(DIFF21_PATH, 'r') as file_obj:
        for line in file_obj:
            ls.append(line)
    return ''.join(ls)[:-1]


def test_converted_to_json_str():
    result = converted_to_json_str(True)
    assert result == 'true'
    result = converted_to_json_str(False)
    assert result == 'false'
    result = converted_to_json_str(156)
    assert result == '156'
    result = converted_to_json_str('123.345.234.123')
    assert result == '123.345.234.123'


def test_get_dict_from_json(dict1, dict2):
    result = get_dict_from_json(JSON_PATH1)
    assert result == dict1
    result = get_dict_from_json(JSON_PATH2)
    assert result == dict2
    result = get_dict_from_json(WRONG_PATH)
    assert result == {}
    result = get_dict_from_json(JSON_WRONG_TYPE_PATH)
    assert result == {}


def test_get_flat_jsons_diff(diff12, diff21):
    result = get_flat_jsons_diff(JSON_PATH1, JSON_PATH2)
    assert result == diff12
    result = get_flat_jsons_diff(JSON_PATH2, JSON_PATH1)
    assert result == diff21
    result = get_flat_jsons_diff(WRONG_PATH, JSON_PATH1)
    assert result == 'Unable to find json-files. Check the paths/types of files'
    result = get_flat_jsons_diff(JSON_WRONG_TYPE_PATH, JSON_PATH1)
    assert result == 'Unable to find json-files. Check the paths/types of files'
