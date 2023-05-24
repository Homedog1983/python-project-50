from gendiff.diff_abstraction import is_line, is_diff, is_updated
from gendiff.diff_abstraction import get_key, get_value, get_children, get_sign


def get_formatted_value(node):
    if is_line(node):
        value = get_value(node)
        if value is None:
            return 'null'
        elif isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, str):
            return f"'{str(value)}'"
        else:
            return value
    return '[complex value]'


def add_line_from_moved(node, lines, path=''):
    result = [f"Property '{path[1:]}' was "]
    if get_sign(node) == '-':
        result.append('removed')
    else:
        result.append(f'added with value: {get_formatted_value(node)}')
    lines.append(''.join(result))


def add_line_from_updated(node, stack, lines, path=''):
    stack.append(node)
    if len(stack) == 2:
        result = [f"Property '{path[1:]}' was updated. From "]
        value2 = get_formatted_value(stack.pop())
        value1 = get_formatted_value(stack.pop())
        result.append(f'{value1} to {value2}')
        lines.append(''.join(result))


def stringify(tree):
    lines = []
    node_stack = []

    def add_lines_from(node, path=''):
        children = get_children(node)
        for sub_node in children:
            sub_key = get_key(sub_node)
            sign = get_sign(sub_node)
            sub_path = f"{path}.{sub_key}"
            if sign != ' ':
                if is_updated(sub_node):
                    add_line_from_updated(sub_node, node_stack, lines, sub_path)
                else:
                    add_line_from_moved(sub_node, lines, sub_path)
            elif is_diff(sub_node):
                add_lines_from(sub_node, sub_path)

    add_lines_from(tree)
    lines_filtered = filter(lambda x: x is not None, lines)
    return '\n'.join(lines_filtered)
