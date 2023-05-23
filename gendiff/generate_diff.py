from gendiff.file_parser import get_dict_from_file
from gendiff.diff_abstraction import make_diff, make_line
import gendiff.stylish as stylish


# def formatted(value) -> str:
#     if value is None:
#         return 'null'
#     elif isinstance(value, bool):
#         return str(value).lower()
#     return str(value)


# def get_plain_diff_line(key, value, sign=' ', indent='  ') -> str:
#     return f'{indent}{sign} {formatted(key)}: {formatted(value)}'


# def get_plain_diff(path1, path2) -> str:
#     dict1 = get_dict_from_file(path1)
#     dict2 = get_dict_from_file(path2)
#     if dict1 == {} or dict2 == {}:
#         return 'No supported file(s). Check the types/paths of them!'
#     union_keys = dict1.keys() | dict2.keys()
#     sorted_keys = sorted(list(union_keys))
#     result = ['{']
#     for key in sorted_keys:
#         value1 = dict1.get(key)
#         value2 = dict2.get(key)
#         if key not in dict1:
#             result.append(get_plain_diff_line(key, value2, '+'))
#         elif key not in dict2:
#             result.append(get_plain_diff_line(key, value1, '-'))
#         elif value1 == value2:
#             result.append(get_plain_diff_line(key, value1))
#         else:
#             result.append(get_plain_diff_line(key, value1, '-'))
#             result.append(get_plain_diff_line(key, value2, '+'))
#     result.append('}')
#     return '\n'.join(result)


def get_mapping_to_diff(key, data, sign=' '):
    if not isinstance(data, dict):
        return make_line(key, data, sign)
    children = []
    for sub_key, sub_data in data.items():
        children.append(get_mapping_to_diff(sub_key, sub_data))
    return make_diff(key, children, sign)


def get_diff_of_dicts(dict1, dict2, key=''):
    union_keys = dict1.keys() | dict2.keys()
    sorted_keys = sorted(list(union_keys))
    children = []
    for sub_key in sorted_keys:
        value1 = dict1.get(sub_key)
        value2 = dict2.get(sub_key)
        if sub_key not in dict2:
            children.append(get_mapping_to_diff(sub_key, value1, '-'))
        elif sub_key not in dict1:
            children.append(get_mapping_to_diff(sub_key, value2, '+'))
        else:
            if value1 == value2:
                children.append(get_mapping_to_diff(sub_key, value1))
            elif isinstance(value1, dict) and isinstance(value2, dict):
                children.append(get_diff_of_dicts(value1, value2, sub_key))
            else:
                children.append(get_mapping_to_diff(sub_key, value1, '-'))
                children.append(get_mapping_to_diff(sub_key, value2, '+'))
    return make_diff(key, children)


def get_nested_diff(path1, path2, formatter=stylish):
    dict1 = get_dict_from_file(path1)
    dict2 = get_dict_from_file(path2)
    if dict1 == {} or dict2 == {}:
        return 'No supported file(s). Check the types/paths of them!'
    diff_tree = get_diff_of_dicts(dict1, dict2)
    diff = formatter.stringify(diff_tree)
    return diff
