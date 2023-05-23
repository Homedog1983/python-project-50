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
    replaced_key = f"{replacer_to_sign}{sign} {get_formatted(key)}: "
    replaced_key_with_zero_factor = replaced_key * int(bool(level))
    replaced_bracket = f"{replacer_to_bracket}" * int(bool(level)) + "}"
    return replaced_key_with_zero_factor, replaced_bracket


def stringify(obj, level=0) -> str:
    key = get_key(obj)
    sign = get_sign(obj)
    replaced_key, replaced_bracket = replaced(key, sign, level)
    if is_line(obj):
        value = get_value(obj)
        return replaced_key + f"{get_formatted(value)}"
    else:
        children = get_children(obj)
        lines = [replaced_key + "{"]
        for obj in children:
            lines.append(f"{stringify(obj, level + 1)}")
    lines.append(replaced_bracket)
    return '\n'.join(lines)
