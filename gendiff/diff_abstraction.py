def make_line(key, value='', status='unchanged'):
    return {
        'key': key,
        'value': value,
        # if 'updated' -> value = {'was': .., 'is': ..}
        'status': status,
        # 'unchanged', 'added', 'removed', 'updated'
        'type': 'line',
    }


def make_diff(key='', children=[]):
    return {
        'key': key,
        'children': children,
        'type': 'diff'
    }


def is_diff(node):
    return node['type'] == 'diff'


def is_line(node):
    return node['type'] == 'line'


def get_key(node):
    return node['key']


def get_value(node):
    return node.get('value', '')


def get_status(node):
    return node.get('status', '')


def get_children(node):
    return node.get('children', [])
