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


# v0.7.11
# def make_line(key, value='', sign=' ', is_updated=False):
#     return {
#         'key': key,
#         'value': value,
#         'sign': sign,
#         'type': 'line',
#         'is_updated': is_updated
#     }


# def make_diff(key='', children=[], sign=' ', is_updated=False):
#     return {
#         'key': key,
#         'children': children,
#         'sign': sign,
#         'type': 'diff',
#         'is_updated': is_updated
#     }


# def is_diff(node):
#     return node['type'] == 'diff'


# def is_line(node):
#     return node['type'] == 'line'


# def is_updated(node):
#     return node['is_updated']


# def get_key(node):
#     return node['key']


# def get_value(line):
#     return line.get('value', '')


# def get_children(node):
#     return node.get('children', [])


# def get_sign(node):
#     return node['sign']
