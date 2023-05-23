def make_line(key, value='', sign=' '):
    """Return line node."""
    return {
        'key': key,
        'value': value,
        'sign': sign,
        'type': 'line'
    }


def make_diff(key='', children=[], sign=' '):
    """Return diff node."""
    return {
        'key': key,
        'children': children,
        'sign': sign,
        'type': 'diff'
    }


def is_diff(node):
    return node['type'] == 'diff'


def is_line(node):
    return node['type'] == 'line'


def get_key(node):
    return node['key']


def get_value(line):
    return line.get('value', '')


def get_children(diff):
    return diff.get('children', [])


def get_sign(node):
    return node['sign']
