from json import load as json_load
from json.decoder import JSONDecodeError
from yaml import safe_load as yaml_load
from yaml.parser import ParserError


def parse(content_file, parse_type):
    if parse_type == 'json':
        parser = json_load
    elif parse_type == 'yaml':
        parser = yaml_load
    else:
        raise ValueError('Unsupported file format')
    try:
        return parser(content_file)
    except (JSONDecodeError, ParserError):
        raise ValueError('Data in file{s) does not match the format json/yaml')


def get_dict_from_file(path):
    if path.endswith('.json'):
        parse_type = 'json'
    elif path.endswith('.yaml') or path.endswith('.yml'):
        parse_type = 'yaml'
    else:
        parse_type = 'other'
    with open(path) as content_file:
        result_dict = parse(content_file, parse_type)
    return result_dict
