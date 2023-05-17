from json import load as json_load
from yaml import safe_load as yaml_safe_load


def get_dict_from_file(path) -> dict:
    dict = {}
    try:
        with open(path, "r") as file:
            if path.endswith('.json'):
                # print('json-format')
                dict = json_load(file)
            elif path.endswith('.yaml') or path.endswith('.yml'):
                # print('yaml-format')
                dict = yaml_safe_load(file)
        return dict
    except (OSError, ValueError):
        # print('error')
        return {}


# paths = {
#     'json1_r': 'tests/fixtures/file1_r.json',
#     'json2_r': 'tests/fixtures/file2_r.json',
#     'yaml1_r': 'tests/fixtures/file1_r.yaml',
#     'yaml2_r': 'tests/fixtures/file2_r.yaml',
# }

# dict1j = get_dict_from_file(paths['json1_r'])
# dict2j = get_dict_from_file(paths['json2_r'])
# dict1y = get_dict_from_file(paths['yaml1_r'])
# dict2y = get_dict_from_file(paths['yaml2_r'])

# print(dict1j == dict1y)
# print(dict2j == dict2y)
