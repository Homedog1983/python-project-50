from json import load as json_load
from yaml import safe_load as yaml_load


def get_parsed(path):
    result_dict = {}
    with open(path, "r") as file:
        if path.endswith('.json'):
            result_dict = json_load(file)
        elif path.endswith('.yaml') or path.endswith('.yml'):
            result_dict = yaml_load(file)
    return result_dict


def get_dict_from_file(path) -> dict:
    try:
        return get_parsed(path)
    except (OSError, ValueError):
        return {}
