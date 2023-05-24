from gendiff.diff_abstraction import is_line
from gendiff.diff_abstraction import get_key, get_value, get_children, get_sign


def get_formatted(value) -> str:
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def replaced(key, sign=' ', level=0, replacer=' ', replacer_per_level=4) -> str:
    signs_to_key = replacer_per_level * level
    replacer_to_bracket = replacer * signs_to_key
    replacer_to_sign = replacer * (signs_to_key - 2)
    replaced_key = f"{replacer_to_sign}{sign} {get_formatted(key)}"
    replaced_bracket = f"{replacer_to_bracket}" + "}"
    return replaced_key, replaced_bracket


def stringify(tree):
    lines = ['{']

    def walk(node, level=0):
        children = get_children(node)
        for sub_node in children:
            key = get_key(sub_node)
            sign = get_sign(sub_node)
            next_level = level + 1
            replaced_key, replaced_bracket = replaced(key, sign, next_level)
            if is_line(sub_node):
                value = get_value(sub_node)
                lines.append(f"{replaced_key}: {get_formatted(value)}")
            else:
                lines.append(f"{replaced_key}: " + "{")
                walk(sub_node, next_level)
                lines.append(f"{replaced_bracket}")
    walk(tree)
    lines.append('}')
    return '\n'.join(lines)
