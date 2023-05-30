from gendiff.diff_abstraction import make_node, get_from
import pytest


@pytest.fixture
def objs():
    children = [make_node('data_key2', 'removed', data='data_2')]
    objs = {
        'data': make_node('data_key1', 'added', data='data_1'),
        'parent': make_node('parent_key', 'parent', children=children)
    }
    return objs


def test_diff_abstraction(objs):
    assert get_from(objs['data'], 'status') == 'added'
    assert get_from(objs['data'], 'status', 'data') == ('added', 'data_1')
    assert objs['data']['status'] == 'added'
    assert objs['data']['children'] == []
    assert objs['parent']['data'] == ''
    assert objs['data']['key'] == 'data_key1'
    assert objs['parent']['status'] == 'parent'
    assert objs['parent']['children'][0]['key'] == 'data_key2'
