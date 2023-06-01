def make_node(key, status, data='', children=[]):
    return {
        'key': key,
        'status': status,
        # 'unchanged', 'added', 'removed', 'updated' - with not-empty data
        # 'parent' - with not-empty children
        'data': data,
        # if 'updated', then data = {'was': .., 'is': ..}
        'children': children
    }


def get_from(node, *property_names):
    if len(property_names) == 1:
        return node[property_names[0]]
    return tuple(map(lambda name: node[name], property_names))
