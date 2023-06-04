from os.path import dirname, abspath
import pytest
from gendiff.generate_diff import get_nested_diff


TESTS_DIR = dirname(abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


def get_fixture_path(file):
    return f"{FIXTURES_PATH}/{file}"


@pytest.mark.parametrize("file1, file2, format, result", [
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
def test_get_nested_diff(file1, file2, format, result):
    file1_path, file2_path, result_path = map(
        get_fixture_path, (file1, file2, result))
    with open(result_path) as result_file:
        result_expected = result_file.read()
        assert get_nested_diff(
            file1_path, file2_path, format) == result_expected
