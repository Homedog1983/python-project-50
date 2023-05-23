import pytest
# from gendiff.generate_diff import get_plain_diff_line
# from gendiff.generate_diff import get_plain_diff
from gendiff.generate_diff import get_nested_diff


@pytest.fixture
def paths():
    paths = {
          'json1': 'tests/fixtures/file1.json',
          'json2': 'tests/fixtures/file2.json',
          'yml1': 'tests/fixtures/file1.yml',
          'yml2': 'tests/fixtures/file2.yml',
          'yaml2': 'tests/fixtures/file2.yaml',
          'not_exist': 'tests/fixtures/f.json',
          'wrong_type': 'tests/fixtures/wrong_type.txt',
          'diff12': 'tests/fixtures/flat_diff12.txt',
          'diff21': 'tests/fixtures/flat_diff21.txt',
          'json1_nested': 'tests/fixtures/file1_nested.json',
          'json2_nested': 'tests/fixtures/file2_nested.json',
          'yaml1_nested': 'tests/fixtures/file1_nested.yaml',
          'yaml2_nested': 'tests/fixtures/file2_nested.yaml',
          'nested_diff12': 'tests/fixtures/nested_diff12.txt'
          }
    return paths


@pytest.fixture
def expected_diffs(paths):
    diffs = {}
    with open(paths['diff12']) as diff12:
        diffs['12'] = diff12.read()
    with open(paths['diff21']) as diff21:
        diffs['21'] = diff21.read()
    with open(paths['nested_diff12']) as nested_diff12:
        diffs['nested_12'] = nested_diff12.read()
    diffs['wrong'] = "No supported file(s). Check the types/paths of them!"
    return diffs


# def test_get_plain_diff_line():
#     result = get_plain_diff_line('1', True)
#     assert result == '    1: true'
#     result = get_plain_diff_line('1', None)
#     assert result == '    1: null'
#     result = get_plain_diff_line('2', False, '+')
#     assert result == '  + 2: false'
#     result = get_plain_diff_line('3', 'True', '-')
#     assert result == '  - 3: True'
#     result = get_plain_diff_line('4', 15)
#     assert result == '    4: 15'
#     result = get_plain_diff_line('5', 'any line', '-')
#     assert result == '  - 5: any line'


# def test_get_plain_diff(paths, expected_diffs):
#     # json-json
#     result = get_plain_diff(paths['json1'], paths['json2'])
#     assert result == expected_diffs['12']
#     result = get_plain_diff(paths['json2'], paths['json1'])
#     assert result == expected_diffs['21']
#     # yml-yml-yaml
#     result = get_plain_diff(paths['yml1'], paths['yml2'])
#     assert result == expected_diffs['12']
#     result = get_plain_diff(paths['yml2'], paths['yml1'])
#     assert result == expected_diffs['21']
#     result = get_plain_diff(paths['yml1'], paths['yaml2'])
#     assert result == expected_diffs['12']
#     result = get_plain_diff(paths['yaml2'], paths['yml1'])
#     assert result == expected_diffs['21']
#     # yml-json
#     result = get_plain_diff(paths['yml1'], paths['json2'])
#     assert result == expected_diffs['12']
#     result = get_plain_diff(paths['yaml2'], paths['json1'])
#     assert result == expected_diffs['21']
#     # wrongs
#     result = get_plain_diff(paths['not_exist'], paths['json1'])
#     assert result == expected_diffs['wrong']
#     result = get_plain_diff(paths['wrong_type'], paths['json2'])
#     assert result == expected_diffs['wrong']
#     result = get_plain_diff(paths['not_exist'], paths['yml1'])
#     assert result == expected_diffs['wrong']
#     result = get_plain_diff(paths['wrong_type'], paths['yaml2'])
#     assert result == expected_diffs['wrong']


def test_get_nested_diff(paths, expected_diffs):
    # plain-json-json
    result = get_nested_diff(paths['json1'], paths['json2'])
    assert result == expected_diffs['12']
    result = get_nested_diff(paths['json2'], paths['json1'])
    assert result == expected_diffs['21']
    # yml-yml-yaml
    result = get_nested_diff(paths['yml1'], paths['yml2'])
    assert result == expected_diffs['12']
    result = get_nested_diff(paths['yml2'], paths['yml1'])
    assert result == expected_diffs['21']
    result = get_nested_diff(paths['yml1'], paths['yaml2'])
    assert result == expected_diffs['12']
    result = get_nested_diff(paths['yaml2'], paths['yml1'])
    assert result == expected_diffs['21']
    # yml-json
    result = get_nested_diff(paths['yml1'], paths['json2'])
    assert result == expected_diffs['12']
    result = get_nested_diff(paths['yaml2'], paths['json1'])
    assert result == expected_diffs['21']
    # wrongs
    result = get_nested_diff(paths['not_exist'], paths['json1'])
    assert result == expected_diffs['wrong']
    result = get_nested_diff(paths['wrong_type'], paths['json2'])
    assert result == expected_diffs['wrong']
    result = get_nested_diff(paths['not_exist'], paths['yml1'])
    assert result == expected_diffs['wrong']
    result = get_nested_diff(paths['wrong_type'], paths['yaml2'])
    assert result == expected_diffs['wrong']
    # nested-json-json
    result = get_nested_diff(paths['json1_nested'], paths['json2_nested'])
    assert result == expected_diffs['nested_12']
