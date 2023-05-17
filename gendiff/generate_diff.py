from gendiff.file_parser import get_dict_from_file


def get_diff_line(sign, key, value) -> str:
    if type(value) == bool:
        value = f'{value}'.lower()
    return f'  {sign} {key}: {value}'


def get_diff(path1, path2) -> str:
    dict1 = get_dict_from_file(path1)
    dict2 = get_dict_from_file(path2)
    if dict1 == {} or dict2 == {}:
        return 'No supported file(s). Check the types/paths of them!'
    keys_union = dict1.keys() | dict2.keys()
    sorted_keys = sorted(list(keys_union))
    result = ['{']
    for key in sorted_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key not in dict1:
            result.append(get_diff_line('+', key, value2))
        elif key not in dict2:
            result.append(get_diff_line('-', key, value1))
        elif value1 == value2:
            result.append(get_diff_line(' ', key, value1))
        else:
            result.append(get_diff_line('-', key, value1))
            result.append(get_diff_line('+', key, value2))
    result.append('}\n')
    return '\n'.join(result)
