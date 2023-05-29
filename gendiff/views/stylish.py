from gendiff.diff_abstraction import is_line
from gendiff.diff_abstraction import get_key, get_value, get_children, get_sign


def to_str(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def get_indents(level=0, replacer=' ', replacer_per_level=4):
    signs_to_key = replacer_per_level * level
    replacer_to_bracket = replacer * signs_to_key
    replacer_to_sign = replacer * (signs_to_key - 2)
    return replacer_to_sign, replacer_to_bracket


def add_lines_from(node, lines, level=0):
    children = get_children(node)
    for sub_node in children:
        key = get_key(sub_node)
        sign = get_sign(sub_node)
        next_level = level + 1
        sign_indent, bracket_indent = get_indents(next_level)
        if is_line(sub_node):
            value = get_value(sub_node)
            lines.append(
                f"{sign_indent}{sign} {to_str(key)}: {to_str(value)}")
        else:
            lines.append(
                f"{sign_indent}{sign} {to_str(key)}: " + "{")
            add_lines_from(sub_node, lines, next_level)
            lines.append(f"{bracket_indent}" + '}')


def stringify(tree):
    lines = ['{']
    add_lines_from(tree, lines)
    lines.append('}')
    return '\n'.join(lines)
