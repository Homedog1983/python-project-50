from gendiff.diff_abstraction import is_line, is_diff, is_updated
from gendiff.diff_abstraction import get_key, get_value, get_children, get_sign


def get_formatted_value(node):
    if is_line(node):
        value = get_value(node)
        if value is None:
            return 'null'
        elif isinstance(value, bool):
            return str(value).lower()
        else:
            return f"'{str(value)}'"
    return '[complex value]'


def get_line_of_moved(node, path=''):
    result = [f"Property '{path[1:]}' was "]
    if get_sign(node) == '-':
        result.append('removed')
    else:
        result.append(f'added with value: {get_formatted_value(node)}')
    return ''.join(result)


def get_line_of_updated(node, stack, path=''):
    stack.append(node)
    if len(stack) == 2:
        result = [f"Property '{path[1:]}' was updated. From "]
        value2 = get_formatted_value(stack.pop())
        value1 = get_formatted_value(stack.pop())
        result.append(f'{value1} to {value2}')
        return ''.join(result)


def stringify(tree):
    lines = []
    updated_stack = []

    def walk(node, path=''):
        children = get_children(node)
        for sub_node in children:
            sub_key = get_key(sub_node)
            sign = get_sign(sub_node)
            sub_path = f"{path}.{sub_key}"
            if sign != ' ':
                if is_updated(sub_node):
                    lines.append(
                        get_line_of_updated(sub_node, updated_stack, sub_path))
                else:
                    lines.append(
                        get_line_of_moved(sub_node, sub_path))
            elif is_diff(sub_node):
                walk(sub_node, sub_path)
    walk(tree)
    lines_filtered = filter(lambda x: x is not None, lines)
    return '\n'.join(lines_filtered)
