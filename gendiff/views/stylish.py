from gendiff.diff_abstraction import get_properties_from


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
    line_start = f"{sign_indent}{sign} {key}: "
    if not isinstance(data, dict):
        lines.append(line_start + f"{to_str(data)}")
    else:
        lines.append(line_start + "{")
        sign = get_sign_from('unchanged')
        for sub_key, sub_data in data.items():
            lines.extend(
                get_lines_from_elem(sign, sub_key, sub_data, level + 1))
        lines.append(f"{bracket_indent}" + '}')
    return lines


def stringify(tree, level=0):
    lines = []
    key, children = get_properties_from(tree, 'key', 'children')
    _, bracket_indent = get_indents(level)
    level_factor = 1 if level > 0 else 0
    lines.append(f"{bracket_indent}{key}: " * level_factor + "{")
    for node in children:
        key, status, data = get_properties_from(node, 'key', 'status', 'data')
        sign = get_sign_from(status)
        if status == 'parent':
            lines.append(stringify(node, level + 1))
            continue
        if status == 'updated':
            lines.extend(
                get_lines_from_elem(sign['was'], key, data['was'], level + 1))
            lines.extend(
                get_lines_from_elem(sign['is'], key, data['is'], level + 1))
            continue
        lines.extend(get_lines_from_elem(sign, key, data, level + 1))
    lines.append(f"{bracket_indent}" + '}')
    return '\n'.join(lines)
