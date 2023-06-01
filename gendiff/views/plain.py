from gendiff.diff_abstraction import get_from


def to_str(data):
    if isinstance(data, dict):
        return '[complex value]'
    if data is None:
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    if isinstance(data, str):
        return f"'{str(data)}'"
    return data


def get_lines_from(tree, path=''):
    lines = []
    children = get_from(tree, 'children')
    for node in children:
        key, status, data = get_from(node, 'key', 'status', 'data')
        next_path = f"{path}.{key}"
        line_start = f"Property '{next_path[1:]}' was"
        if status == 'removed':
            lines += [f'{line_start} removed']
            continue
        if status == 'added':
            lines += [f'{line_start} added with value: {to_str(data)}']
            continue
        if status == 'updated':
            data_1 = to_str(data['was'])
            data_2 = to_str(data['is'])
            lines += [f'{line_start} updated. From {data_1} to {data_2}']
            continue
        if status == 'unchanged':
            continue
        lines += get_lines_from(node, next_path)
    return lines


def stringify(tree):
    return '\n'.join(get_lines_from(tree))
