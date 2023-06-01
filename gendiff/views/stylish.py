from gendiff.diff_abstraction import get_from


def to_str(data):
    if data is None:
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    return str(data)


def get_sign_from(status):
    signs = {
        'unchanged': ' ',
        'added': '+',
        'removed': '-',
        'updated': {
            'was': '-',
            'is': '+'
        },
        'parent': ' '
    }
    return signs.get(status, ' ')


def get_indents(level, replacer=' ', replacer_per_level=4):
    signs_to_key = replacer_per_level * level
    indent_to_bracket = replacer * signs_to_key
    indent_to_sign = replacer * (signs_to_key - 2)
    return indent_to_sign, indent_to_bracket


def get_lines_from_elem(sign, key, data, level):
    lines = []
    sign_indent, bracket_indent = get_indents(level)
    line_start = f"{sign_indent}{sign} {to_str(key)}: "
    if not isinstance(data, dict):
        lines += [line_start + f"{to_str(data)}"]
    else:
        lines += [line_start + "{"]
        sign = get_sign_from('unchanged')
        for sub_key, sub_data in data.items():
            lines += get_lines_from_elem(sign, sub_key, sub_data, level + 1)
        lines += [f"{bracket_indent}" + '}']
    return lines


def get_lines_from(tree, level=0):
    lines = []
    children = get_from(tree, 'children')
    level += 1
    for node in children:
        key, status, data = get_from(node, 'key', 'status', 'data')
        sign = get_sign_from(status)
        if status == 'parent':
            _, bracket_indent = get_indents(level)
            lines += [f"{bracket_indent}{to_str(key)}: " + "{"]
            lines += get_lines_from(node, level)
            lines += [f"{bracket_indent}" + '}']
            continue
        if status == 'updated':
            lines += get_lines_from_elem(sign['was'], key, data['was'], level)
            lines += get_lines_from_elem(sign['is'], key, data['is'], level)
            continue
        lines += get_lines_from_elem(sign, key, data, level)
    return lines


def stringify(tree):
    return '\n'.join(['{'] + get_lines_from(tree) + ['}'])
