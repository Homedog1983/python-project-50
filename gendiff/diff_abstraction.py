def make_line(key, value='', sign=' ', is_updated=False):
    return {
        'key': key,
        'value': value,
        'sign': sign,
        'type': 'line',
        'is_updated': is_updated
    }


def make_diff(key='', children=[], sign=' ', is_updated=False):
    return {
        'key': key,
        'children': children,
        'sign': sign,
        'type': 'diff',
        'is_updated': is_updated
    }


def is_diff(node):
    return node['type'] == 'diff'


def is_line(node):
    return node['type'] == 'line'


def is_updated(node):
    return node['is_updated']


def get_key(node):
    return node['key']


def get_value(line):
    return line.get('value', '')


def get_children(diff):
    return diff.get('children', [])


def get_sign(node):
    return node['sign']
