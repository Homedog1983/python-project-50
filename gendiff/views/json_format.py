from gendiff.diff_abstraction import get_from
from json import dumps


def add_elems_to_dict_from(tree, tree_dict):
    children = get_from(tree, 'children')
    for node in children:
        key, status, data = get_from(node, 'key', 'status', 'data')
        if status == 'removed' or status == 'added':
            tree_dict[key] = [status.upper(), data]
            continue
        if status == 'updated':
            data_1 = data['was']
            data_2 = data['is']
            tree_dict[key] = [status.upper(), data_1, data_2]
            continue
        if status == 'unchanged':
            tree_dict[key] = data
            continue
        sub_dict = {}
        add_elems_to_dict_from(node, sub_dict)
        tree_dict[key] = sub_dict


def stringify(tree):
    tree_dict = {}
    add_elems_to_dict_from(tree, tree_dict)
    return dumps(tree_dict, indent=4)
