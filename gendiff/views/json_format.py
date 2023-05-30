from gendiff.diff_abstraction import is_line, get_key, get_value
from gendiff.diff_abstraction import get_children, get_status
from json import dumps


def add_elems_to_dict_from(tree, tree_dict):
    children = get_children(tree)
    for node in children:
        key = get_key(node)
        if is_line(node):
            status = get_status(node)
            value = get_value(node)
            if status == 'removed' or status == 'added':
                tree_dict[key] = [status.upper(), value]
            elif status == 'updated':
                value_1 = value['was']
                value_2 = value['is']
                tree_dict[key] = [status.upper(), value_1, value_2]
            else:
                tree_dict[key] = value
        else:
            sub_dict = {}
            add_elems_to_dict_from(node, sub_dict)
            tree_dict[key] = sub_dict


def stringify(tree):
    tree_dict = {}
    add_elems_to_dict_from(tree, tree_dict)
    return dumps(tree_dict, indent=4)
