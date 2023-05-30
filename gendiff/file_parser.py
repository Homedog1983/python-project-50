from json import load as json_load
from yaml import safe_load as yaml_load


def parse(content_file, parse_type):
    if parse_type == 'json':
        parser = json_load
    if parse_type == 'yaml':
        parser = yaml_load
    return parser(content_file)


def get_dict_from_file(path):
    result_dict = {}
    if path.endswith('.json'):
        parse_type = 'json'
    elif path.endswith('.yaml') or path.endswith('.yml'):
        parse_type = 'yaml'
    else:
        print("Unsupported file format")
        return result_dict
    try:
        with open(path) as content_file:
            result_dict = parse(content_file, parse_type)
    except (OSError, ValueError) as except_type:
        print(except_type)

    return result_dict
