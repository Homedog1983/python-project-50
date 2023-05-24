from gendiff.file_parser import get_dict_from_file
from gendiff.diff_abstraction import make_diff, make_line
import gendiff.views.stylish as stylish
import gendiff.views.plain as plain
import gendiff.views.json_format as json_format


def get_node_from_item(key, data, sign=' ', is_updated=False):
    if not isinstance(data, dict):
        return make_line(key, data, sign, is_updated)
    children = []
    for sub_key, sub_data in data.items():
        children.append(get_node_from_item(sub_key, sub_data))
    return make_diff(key, children, sign, is_updated)


def get_diff_from_dicts(dict1, dict2, key=''):
    union_keys = dict1.keys() | dict2.keys()
    sorted_keys = sorted(list(union_keys))
    children = []
    for sub_key in sorted_keys:
        value1 = dict1.get(sub_key)
        value2 = dict2.get(sub_key)
        if sub_key not in dict2:
            children.append(get_node_from_item(sub_key, value1, '-'))
        elif sub_key not in dict1:
            children.append(get_node_from_item(sub_key, value2, '+'))
        else:
            if value1 == value2:
                children.append(get_node_from_item(sub_key, value1))
            elif isinstance(value1, dict) and isinstance(value2, dict):
                children.append(get_diff_from_dicts(value1, value2, sub_key))
            else:
                children.append(get_node_from_item(sub_key, value1, '-', True))
                children.append(get_node_from_item(sub_key, value2, '+', True))
    return make_diff(key, children)


def get_nested_diff(path1, path2, format_name='stylish'):
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json_format
    }
    formatter = formats.get(format_name, stylish)
    dict1 = get_dict_from_file(path1)
    dict2 = get_dict_from_file(path2)
    if dict1 == {} or dict2 == {}:
        return 'No supported file(s). Check the types/paths of them!'
    diff_tree = get_diff_from_dicts(dict1, dict2)
    diff = formatter.stringify(diff_tree)
    return diff
