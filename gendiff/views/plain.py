from gendiff.diff_abstraction import get_properties_from


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
    children = get_properties_from(tree, 'children')
    for node in children:
        key, status, data = get_properties_from(node, 'key', 'status', 'data')
        next_path = f"{path}.{key}"
        line_start = f"Property '{next_path[1:]}' was"
        if status == 'unchanged':
            continue
        if status == 'removed':
            lines.append(f'{line_start} removed')
            continue
        if status == 'added':
            lines.append(f'{line_start} added with value: {to_str(data)}')
            continue
        if status == 'updated':
            value_was = to_str(data['was'])
            value_is = to_str(data['is'])
            lines.append(
                f'{line_start} updated. From {value_was} to {value_is}')
            continue
        lines.extend(get_lines_from(node, next_path))
    return lines


def stringify(tree):
    return '\n'.join(get_lines_from(tree))
