from json import load as json_load
from yaml import safe_load as yaml_safe_load


def get_dict_from_file(path) -> dict:
    dict = {}
    try:
        with open(path, "r") as file:
            if path.endswith('.json'):
                dict = json_load(file)
            elif path.endswith('.yaml') or path.endswith('.yml'):
                dict = yaml_safe_load(file)
        return dict
    except (OSError, ValueError):
        return {}
