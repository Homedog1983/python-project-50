from gendiff.diff_abstraction import make_diff, make_line
from gendiff.diff_abstraction import is_diff, is_line, is_updated
from gendiff.diff_abstraction import get_children, get_key, get_sign, get_value
import pytest


@pytest.fixture
def objs():
    children = [make_line('line_2', 'value2', '-')]
    objs = {
        'line': make_line('line_key', 'value', '-', True),
        'diff': make_diff('diff_key', children=[], sign='+', is_updated=False),
        'tree': make_diff('tree_key', children=children, sign='-')
    }
    return objs


def test_diff_abstraction(objs):
    assert is_diff(objs['diff'])
    assert is_line(objs['line'])
    assert is_updated(objs['line'])
    assert not is_updated(objs['diff'])
    assert get_key(objs['diff']) == 'diff_key'
    assert get_key(objs['line']) == 'line_key'
    assert get_sign(objs['diff']) == '+'
    assert get_sign(objs['line']) == '-'
    assert get_value(objs['line']) == 'value'
    children = get_children(objs['tree'])
    assert get_key(children[0]) == 'line_2'
    assert is_line(children[0])
    assert get_sign(children[0]) == '-'
