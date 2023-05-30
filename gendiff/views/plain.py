from gendiff.diff_abstraction import is_line, get_status
from gendiff.diff_abstraction import get_key, get_value, get_children


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{str(value)}'"
    return value


def add_lines_from(tree, lines, path=''):
    children = get_children(tree)
    for node in children:
        key = get_key(node)
        next_path = f"{path}.{key}"
        if is_line(node):
            value = get_value(node)
            line_start = f"Property '{next_path[1:]}' was"
            status = get_status(node)
            if status == 'removed':
                lines.append(f'{line_start} removed')
            elif status == 'added':
                lines.append(f'{line_start} added with value: {to_str(value)}')
            elif status == 'updated':
                value_1 = to_str(value['was'])
                value_2 = to_str(value['is'])
                lines.append(
                    f'{line_start} updated. From {value_1} to {value_2}')
        else:
            add_lines_from(node, lines, next_path)


def stringify(tree):
    tree_lines = []
    add_lines_from(tree, tree_lines)
    return '\n'.join(tree_lines)
