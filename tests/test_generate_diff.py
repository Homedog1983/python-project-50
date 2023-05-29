import pytest
from gendiff.generate_diff import get_nested_diff


@pytest.mark.parametrize("path1, path2, format_name, diff_path", [
    # wrongs -> all formats)
    ('f.json', 'file1.json', 'sdf', 'wrong.txt'),
    ('wrong_type.txt', 'file2.json', 'plain', 'wrong.txt'),
    ('f.json', 'file1.json', 'json', 'wrong.txt'),
    ('wrong_type.txt', 'file2.json', 'stylish', 'wrong.txt'),
    # flat-json-json -> stylish
    ('file1.json', 'file2.json', 'stylish', 'flat_diff12.txt'),
    ('file2.json', 'file1.json', 'dfdf', 'flat_diff21.txt'),
    # # flat yml-yml-yaml -> stylish
    ('file1.yml', 'file2.yml', 'stylish', 'flat_diff12.txt'),
    ('file1.yml', 'file2.yaml', 'sd', 'flat_diff12.txt'),
    ('file2.yaml', 'file1.yml', 'e', 'flat_diff21.txt'),
    # # flat yml-json -> stylish
    ('file1.yaml', 'file2.json', 'stylish', 'flat_diff12.txt'),
    ('file2.yaml', 'file1.json', 'sew', 'flat_diff21.txt'),
    ('file1.json', 'file2.yaml', 'rtyuo', 'flat_diff12.txt'),
    # # nested -> stylish
    ('file1_n.json', 'file2_n.json', 'df', 'nested_12s.txt'),
    ('file1_n.yaml', 'file2_n.yaml', 'stylish', 'nested_12s.txt'),
    ('file1_n.json', 'file2_n.yaml', '', 'nested_12s.txt'),
    # nested -> plain
    ('file1_n.json', 'file2_n.json', 'plain', 'nested_12p.txt'),
    ('file1_n.yaml', 'file2_n.yaml', 'plain', 'nested_12p.txt'),
    ('file1_n.json', 'file2_n.yaml', 'plain', 'nested_12p.txt'),
    # nested -> json
    ('file1_n.json', 'file2_n.json', 'json', 'nested_12j.txt'),
    ('file1_n.yaml', 'file2_n.yaml', 'json', 'nested_12j.txt'),
    ('file1_n.json', 'file2_n.yaml', 'json', 'nested_12j.txt')
])
def test_get_nested_diff(path1, path2, format_name, diff_path):
    fixtures = 'tests/fixtures/'
    full_path1 = f'{fixtures}{path1}'
    full_path2 = f'{fixtures}{path2}'
    full_diff_path = f'{fixtures}{diff_path}'
    with open(full_diff_path) as diff_file:
        diff = diff_file.read()
    assert get_nested_diff(full_path1, full_path2, format_name) == diff
