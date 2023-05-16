import pytest
from gendiff.diffs.flat_jsons_diff import converted_to_json_str
from gendiff.diffs.flat_jsons_diff import get_dict_from_json
from gendiff.diffs.flat_jsons_diff import get_flat_jsons_diff
from tests.fixtures import flat_dicts as data


@pytest.fixture
def paths():
    paths = {
          'json1': 'tests/fixtures/file1.json',
          'json2': 'tests/fixtures/file2.json',
          'yml1': 'tests/fixtures/file1.yml',
          'yml2': 'tests/fixtures/file2.yaml',
          'not_exist': 'tests/fixtures/f.json',
          'wrong_type': 'tests/fixtures/wrong_type.txt',
          'diff12': 'tests/fixtures/flat_diff12.txt',
          'diff21': 'tests/fixtures/flat_diff21.txt'
          }
    return paths


@pytest.fixture
def expected_dicts():
    dicts = {}
    dicts['1'] = data.dict1
    dicts['2'] = data.dict2
    return dicts


@pytest.fixture
def expected_diffs(paths):
    diffs = {}
    with open(paths['diff12']) as diff12:
        diffs['12'] = diff12.read()
    with open(paths['diff21']) as diff21:
        diffs['21'] = diff21.read()
    return diffs


def test_converted_to_json_str():
    result = converted_to_json_str(True)
    assert result == 'true'
    result = converted_to_json_str(False)
    assert result == 'false'
    result = converted_to_json_str(156)
    assert result == '156'
    result = converted_to_json_str('123.345.234.123')
    assert result == '123.345.234.123'


def test_get_dict_from_json(expected_dicts, paths):
    result = get_dict_from_json(paths['json1'])
    assert result == expected_dicts['1']
    result = get_dict_from_json(paths['json2'])
    assert result == expected_dicts['2']
    result = get_dict_from_json(paths['not_exist'])
    assert result == {}
    result = get_dict_from_json(paths['wrong_type'])
    assert result == {}


def test_get_flat_jsons_diff(paths, expected_diffs):
    result = get_flat_jsons_diff(paths['json1'], paths['json2'])
    assert result == expected_diffs['12']
    result = get_flat_jsons_diff(paths['json2'], paths['json1'])
    assert result == expected_diffs['21']
    result = get_flat_jsons_diff(paths['not_exist'], paths['json1'])
    assert result == 'Unable to find json-files. Check the paths/types of files'
    result = get_flat_jsons_diff(paths['wrong_type'], paths['json1'])
    assert result == 'Unable to find json-files. Check the paths/types of files'
