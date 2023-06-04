from json import load as json_load
from yaml import safe_load as yaml_load
from os.path import splitext


def parse(content_file, parser_type):
    if parser_type == 'json':
        return json_load(content_file)
    if parser_type == 'yaml':
        return yaml_load(content_file)
    raise ValueError('Unsupported file format')


def get_dict_from_file(path):
    _, extension = splitext(path)
    if extension == '.json':
        parser_type = 'json'
    elif extension == '.yaml' or extension == '.yml':
        parser_type = 'yaml'
    else:
        parser_type = 'other'
    with open(path) as content_file:
        result_dict = parse(content_file, parser_type)
    return result_dict
