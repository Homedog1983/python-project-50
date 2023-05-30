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


def add_lines_from(tree, lines, path=''):
    children = get_from(tree, 'children')
    for node in children:
        key, status, data = get_from(node, 'key', 'status', 'data')
        next_path = f"{path}.{key}"
        line_start = f"Property '{next_path[1:]}' was"
        if status == 'removed':
            lines.append(f'{line_start} removed')
            continue
        if status == 'added':
            lines.append(f'{line_start} added with value: {to_str(data)}')
            continue
        if status == 'updated':
            data_1 = to_str(data['was'])
            data_2 = to_str(data['is'])
            lines.append(
                f'{line_start} updated. From {data_1} to {data_2}')
            continue
        if status == 'unchanged':
            continue
        add_lines_from(node, lines, next_path)


def stringify(tree):
    tree_lines = []
    add_lines_from(tree, tree_lines)
    return '\n'.join(tree_lines)
