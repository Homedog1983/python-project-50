from gendiff.file_parser import get_dict_from_file
from gendiff.diff_abstraction import make_node
from gendiff.views.generate_veiw import get_view_from


def get_diff_from_dicts(dict1, dict2, node_key=''):
    union_keys = dict1.keys() | dict2.keys()
    sorted_keys = sorted(list(union_keys))
    children = []
    for key in sorted_keys:
        data_1 = dict1.get(key)
        data_2 = dict2.get(key)
        if key not in dict2:
            children.append(make_node(key, 'removed', data_1))
            continue
        if key not in dict1:
            children.append(make_node(key, 'added', data_2))
            continue
        if data_1 == data_2:
            children.append(make_node(key, 'unchanged', data_1))
            continue
        if isinstance(data_1, dict) and isinstance(data_2, dict):
            children.append(get_diff_from_dicts(data_1, data_2, key))
            continue
        data = {
            'was': data_1,
            'is': data_2
        }
        children.append(make_node(key, 'updated', data))
    return make_node(node_key, 'parent', children=children)


def get_nested_diff(path1, path2, format_type):
    dict1 = get_dict_from_file(path1)
    dict2 = get_dict_from_file(path2)
    diff_tree = get_diff_from_dicts(dict1, dict2)
    return get_view_from(diff_tree, format_type)
