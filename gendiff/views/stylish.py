from gendiff.diff_abstraction import get_from


def to_str(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def get_sign_from(status):
    signs = {
        'unchanged': ' ',
        'added': '+',
        'removed': '-',
        'updated': {'was': '-', 'is': '+'},
        'parent': ' '
    }
    return signs.get(status, ' ')


def get_indents(level, replacer=' ', replacer_per_level=4):
    signs_to_key = replacer_per_level * level
    indent_to_bracket = replacer * signs_to_key
    indent_to_sign = replacer * (signs_to_key - 2)
    return indent_to_sign, indent_to_bracket


def add_lines_from_elem(sign, key, data, level, lines):
    sign_indent, bracket_indent = get_indents(level)
    line_start = f"{sign_indent}{sign} {to_str(key)}: "
    if not isinstance(data, dict):
        lines.append(line_start + f"{to_str(data)}")
    else:
        lines.append(line_start + "{")
        sign = get_sign_from('unchanged')
        for sub_key, sub_value in data.items():
            add_lines_from_elem(sign, sub_key, sub_value, level + 1, lines)
        lines.append(f"{bracket_indent}" + '}')


def add_lines_from(tree, level, lines):
    children = get_from(tree, 'children')
    level += 1
    for node in children:
        key, status, data = get_from(node, 'key', 'status', 'data')
        sign = get_sign_from(status)
        if status == 'parent':
            _, bracket_indent = get_indents(level)
            lines.append(f"{bracket_indent}{to_str(key)}: " + "{")
            add_lines_from(node, level, lines)
            lines.append(f"{bracket_indent}" + '}')
            continue
        if status == 'updated':
            add_lines_from_elem(sign['was'], key, data['was'], level, lines)
            add_lines_from_elem(sign['is'], key, data['is'], level, lines)
            continue
        add_lines_from_elem(sign, key, data, level, lines)


def stringify(tree):
    lines = ['{']
    add_lines_from(tree, 0, lines)
    lines.append('}')
    return '\n'.join(lines)
