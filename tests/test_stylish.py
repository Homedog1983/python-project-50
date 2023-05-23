from gendiff.diff_abstraction import make_diff, make_line
from gendiff.stylish import stringify
import pytest


@pytest.fixture
def paths():
    paths = {
        'simple_nested_diff': 'tests/fixtures/simple_nested_diff.txt'
    }
    return paths


@pytest.fixture
def expected_stringifies(paths):
    expected_stringifies = {}
    with open(paths['simple_nested_diff']) as simple_diff_file:
        expected_stringifies['simple_diff'] = simple_diff_file.read()
    return expected_stringifies


@pytest.fixture
def diff_trees():
    diff_trees = {}
    children_nested = [
        make_line('key3', 'value3', ' '),
        make_line('key4', 'value4', ' ')
    ]
    children = [
        make_line('key1', 'value1_1', '-'),
        make_line('key1', 'value1_2', '+'),
        make_diff('key2', children=children_nested, sign='-'),
        make_line('key2', 'value2_2', sign='+'),
        make_line('key5', 'value5', '+')
    ]
    diff_trees['simple'] = make_diff(key='root', children=children, sign=' ')
    return diff_trees


def test_stringify(diff_trees, expected_stringifies):
    result = stringify(diff_trees['simple'])
    assert result == expected_stringifies['simple_diff']
