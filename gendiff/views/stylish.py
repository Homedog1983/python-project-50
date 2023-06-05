from gendiff.diff_abstraction import get_properties_from


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


def sign_indent(lvl, replacer=' ', replacer_per_lvl=4):
    return replacer * (replacer_per_lvl * lvl - 2)


def bracket_indent(lvl, replacer=' ', replacer_per_lvl=4):
    return replacer * (replacer_per_lvl * lvl)


def to_str(data, lvl=0):
    if isinstance(data, dict):
        lines = ['{']
        sign = get_sign_from('unchanged')
        indent = sign_indent(lvl + 1)
        for sub_key, sub_data in data.items():
            lines.append(
                f"{indent}{sign} {sub_key}: {to_str(sub_data, lvl + 1)}")
        lines.append(f"{bracket_indent(lvl)}" + '}')
        return '\n'.join(lines)
    if data is None:
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    return str(data)


def stringify(tree, lvl=0):
    lines = []
    key, children = get_properties_from(tree, 'key', 'children')
    lvl_factor = 1 if lvl > 0 else 0
    lines.append(f"{bracket_indent(lvl)}{key}: " * lvl_factor + "{")
    indent = sign_indent(lvl + 1)
    for node in children:
        key, status, data = get_properties_from(node, 'key', 'status', 'data')
        sign = get_sign_from(status)
        if status == 'parent':
            lines.append(stringify(node, lvl + 1))
            continue
        if status == 'updated':
            lines.append(
                f"{indent}{sign['was']} {key}: {to_str(data['was'], lvl + 1)}")
            lines.append(
                f"{indent}{sign['is']} {key}: {to_str(data['is'], lvl + 1)}")
            continue
        lines.append(f"{indent}{sign} {key}: {to_str(data, lvl + 1)}")
    lines.append(f"{bracket_indent(lvl)}" + '}')
    return '\n'.join(lines)
