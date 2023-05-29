from json import load as json_load
from yaml import safe_load as yaml_load


def parse(content_file, parse_type):
    parser = json_load if parse_type == 'json' else yaml_load
    return parser(content_file)


def get_dict_from_file(path):
    if path.endswith('.json'):
        parse_type = 'json'
    elif path.endswith('.yaml') or path.endswith('.yml'):
        parse_type = 'yaml'
    else:
        return {}
    try:
        with open(path) as file:
            result_dict = parse(file, parse_type)
    except (OSError, ValueError):
        return {}

    return result_dict
