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


def get_properties_from(node, *property_names):
    return tuple(map(lambda name: node[name], property_names))
