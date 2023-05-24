from gendiff.diff_abstraction import is_line, get_key, get_value
from gendiff.diff_abstraction import get_children, get_sign, is_updated
from json import dumps


def get_data(node):
    if is_line(node):
        return get_value(node)
    children = get_children(node)
    result_dict = {}
    for sub_node in children:
        sub_key = get_key(sub_node)
        result_dict[sub_key] = get_data(sub_node)
    return result_dict


def add_moved_to_dict(node, outer_dict):
    key = get_key(node)
    sign = get_sign(node)
    status = "ADDED" if sign == "+" else "REMOVED"
    outer_dict[key] = [status, get_data(node)]


def add_updated_to_dict(node, stack, outer_dict):
    stack.append(node)
    if len(stack) == 2:
        key = get_key(node)
        value2 = get_data(stack.pop())
        value1 = get_data(stack.pop())
        outer_dict[key] = ["UPDATED", value1, value2]


def get_dict_from(tree):
    node_stack = []
    result_dict = {}

    def add_to_dict_from(node, outer_dict):
        children = get_children(node)
        for sub_node in children:
            sign = get_sign(sub_node)
            if sign != ' ':
                if is_updated(sub_node):
                    add_updated_to_dict(sub_node, node_stack, outer_dict)
                else:
                    add_moved_to_dict(sub_node, outer_dict)
            else:
                sub_key = get_key(sub_node)
                if is_line(sub_node):
                    outer_dict[sub_key] = get_value(sub_node)
                else:
                    sub_dict = {}
                    add_to_dict_from(sub_node, sub_dict)
                    outer_dict[sub_key] = sub_dict

    add_to_dict_from(tree, result_dict)
    return result_dict


def stringify(tree, indent=4):
    outer_dict = get_dict_from(tree)
    diff = dumps(outer_dict, indent=indent)
    return diff
