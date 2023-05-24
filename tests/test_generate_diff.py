import pytest
from gendiff.generate_diff import get_nested_diff


def params():
    paths = {
        'json1': 'tests/fixtures/file1.json',
        'json2': 'tests/fixtures/file2.json',
        'yml1': 'tests/fixtures/file1.yml',
        'yml2': 'tests/fixtures/file2.yml',
        'yaml1': 'tests/fixtures/file1.yaml',
        'yaml2': 'tests/fixtures/file2.yaml',
        'not_exist': 'tests/fixtures/f.json',
        'wrong_type': 'tests/fixtures/wrong_type.txt',
        'json1_nested': 'tests/fixtures/file1_nested.json',
        'json2_nested': 'tests/fixtures/file2_nested.json',
        'yaml1_nested': 'tests/fixtures/file1_nested.yaml',
        'yaml2_nested': 'tests/fixtures/file2_nested.yaml',
    }

    diff_paths = {
        'diff12': 'tests/fixtures/flat_diff12.txt',
        'diff21': 'tests/fixtures/flat_diff21.txt',
        'nested_diff12': 'tests/fixtures/nested_diff12.txt',
        'nested_diff12_plain': 'tests/fixtures/nested_diff12_plain.txt',
        'nested_diff12_json': 'tests/fixtures/nested_diff12_json.txt'
    }

    diffs = {}
    with open(diff_paths['diff12']) as diff12:
        diffs['12'] = diff12.read()
    with open(diff_paths['diff21']) as diff21:
        diffs['21'] = diff21.read()
    with open(diff_paths['nested_diff12']) as nested_diff12:
        diffs['n_s'] = nested_diff12.read()
    with open(diff_paths['nested_diff12_plain']) as nested_diff12_plain:
        diffs['n_p'] = nested_diff12_plain.read()
    with open(diff_paths['nested_diff12_json']) as nested_diff12_json:
        diffs['n_j'] = nested_diff12_json.read()
    diffs['wrong'] = "No supported file(s). Check the types/paths of them!"

    return [
        # path1, path2, format_name, expected
        # # wrongs -> all formats)
        (paths['not_exist'], paths['json1'], 'sdf', diffs['wrong']),
        (paths['wrong_type'], paths['json2'], 'plain', diffs['wrong']),
        (paths['not_exist'], paths['json1'], 'json', diffs['wrong']),
        (paths['wrong_type'], paths['json2'], 'stylish', diffs['wrong']),
        # flat-json-json -> stylish
        (paths['json1'], paths['json2'], 'stylish', diffs['12']),
        (paths['json2'], paths['json1'], 'dfdf', diffs['21']),
        # # flat yml-yml-yaml -> stylish
        (paths['yml1'], paths['yml2'], 'stylish', diffs['12']),
        (paths['yml1'], paths['yaml2'], 'sd', diffs['12']),
        (paths['yaml2'], paths['yml1'], 'e', diffs['21']),
        # # flat yml-json -> stylish
        (paths['yaml1'], paths['json2'], 'stylish', diffs['12']),
        (paths['yml2'], paths['json1'], 'sew', diffs['21']),
        (paths['json1'], paths['yml2'], 'rtyuo', diffs['12']),
        # # nested -> stylish
        (paths['json1_nested'], paths['json2_nested'], 'df', diffs['n_s']),
        (paths['yaml1_nested'], paths['yaml2_nested'], 'stylish', diffs['n_s']),
        (paths['json1_nested'], paths['yaml2_nested'], '', diffs['n_s']),
        # # nested -> plain
        (paths['json1_nested'], paths['json2_nested'], 'plain', diffs['n_p']),
        (paths['yaml1_nested'], paths['yaml2_nested'], 'plain', diffs['n_p']),
        (paths['json1_nested'], paths['yaml2_nested'], 'plain', diffs['n_p']),
        # # nested -> json
        (paths['json1_nested'], paths['json2_nested'], 'json', diffs['n_j']),
        (paths['yaml1_nested'], paths['yaml2_nested'], 'json', diffs['n_j']),
        (paths['json1_nested'], paths['yaml2_nested'], 'json', diffs['n_j'])
    ]


@pytest.mark.parametrize("path1, path2, format_name, expected", params())
def test_get_nested_diff(path1, path2, format_name, expected):
    assert get_nested_diff(path1, path2, format_name) == expected
