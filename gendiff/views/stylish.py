from gendiff.diff_abstraction import is_line, get_status
from gendiff.diff_abstraction import get_key, get_value, get_children


def to_str(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def get_indents(level, replacer=' ', replacer_per_level=4):
    signs_to_key = replacer_per_level * level
    replacer_to_bracket = replacer * signs_to_key
    replacer_to_sign = replacer * (signs_to_key - 2)
    return replacer_to_sign, replacer_to_bracket


def get_sign_from(status):
    signs = {
        'unchanged': ' ',
        'added': '+',
        'removed': '-',
        'updated': {'was': '-', 'is': '+'}
    }
    return signs.get(status, ' ')


def add_lines_from_elem(sign, key, value, level, lines):
    sign_indent, bracket_indent = get_indents(level)
    if not isinstance(value, dict):
        lines.append(
            f"{sign_indent}{sign} {to_str(key)}: {to_str(value)}")
    else:
        lines.append(
            f"{sign_indent}{sign} {to_str(key)}: " + "{")
        sign = get_sign_from('unchanged')
        for sub_key, sub_value in value.items():
            add_lines_from_elem(sign, sub_key, sub_value, level + 1, lines)
        lines.append(f"{bracket_indent}" + '}')


def add_lines_from_line_node(node, level, lines):
    key = get_key(node)
    value = get_value(node)
    status = get_status(node)
    sign = get_sign_from(status)
    if status == 'updated':
        add_lines_from_elem(sign['was'], key, value['was'], level, lines)
        add_lines_from_elem(sign['is'], key, value['is'], level, lines)
    else:
        add_lines_from_elem(sign, key, value, level, lines)


def add_lines_from(tree, level, lines):
    children = get_children(tree)
    next_level = level + 1
    for node in children:
        key = get_key(node)
        if is_line(node):
            add_lines_from_line_node(node, next_level, lines)
        else:
            _, bracket_indent = get_indents(next_level)
            lines.append(f"{bracket_indent}{to_str(key)}: " + "{")
            add_lines_from(node, next_level, lines)
            lines.append(f"{bracket_indent}" + '}')


def stringify(tree):
    lines = ['{']
    add_lines_from(tree, 0, lines)
    lines.append('}')
    return '\n'.join(lines)
