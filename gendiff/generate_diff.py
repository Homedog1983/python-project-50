from gendiff.file_parser import get_dict_from_file
from gendiff.diff_abstraction import make_diff, make_line
from gendiff.views.generate_veiw import get_view_from


def get_diff_from_dicts(dict1, dict2, key=''):
    union_keys = dict1.keys() | dict2.keys()
    sorted_keys = sorted(list(union_keys))
    children = []
    for sub_key in sorted_keys:
        value1 = dict1.get(sub_key)
        value2 = dict2.get(sub_key)
        if sub_key not in dict2:
            children.append(make_line(sub_key, value1, 'removed'))
        elif sub_key not in dict1:
            children.append(make_line(sub_key, value2, 'added'))
        else:
            if value1 == value2:
                children.append(make_line(sub_key, value1))
            elif isinstance(value1, dict) and isinstance(value2, dict):
                children.append(get_diff_from_dicts(value1, value2, sub_key))
            else:
                value = {}
                value['was'] = value1
                value['is'] = value2
                children.append(make_line(sub_key, value, 'updated'))

    return make_diff(key, children)


def get_nested_diff(path1, path2, format_name='stylish'):
    dict1 = get_dict_from_file(path1)
    dict2 = get_dict_from_file(path2)
    if dict1 == {} or dict2 == {}:
        return 'No supported file(s). Check the types/paths of them!'
    diff_tree = get_diff_from_dicts(dict1, dict2)
    diff = get_view_from(diff_tree, format_name)
    return diff
