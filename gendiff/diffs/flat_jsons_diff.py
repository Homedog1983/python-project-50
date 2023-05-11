from json import load


def get_dict_from_json(path1) -> dict:
    try:
        with open(path1, "r") as input_file:
            dict = load(input_file)
        return dict
    except (OSError, ValueError):
        return {}


def get_flat_jsons_diff(path1, path2) -> str:
    dict1 = get_dict_from_json(path1)
    dict2 = get_dict_from_json(path2)
    if dict1 == {} or dict2 == {}:
        return 'Unable to find json-files. Check the paths/types of files'
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    union_keys = keys1 | keys2
    sorted_keys = sorted(list(union_keys))
    result = ['{']
    for key in sorted_keys:
        if (key in keys1) and (key in keys2):
            value1 = dict1[key]
            value2 = dict2[key]
            if value1 == value2:
                result += [f'    {key}: {value1}']
            else:
                result += [f'  - {key}: {value1}']
                result += [f'  + {key}: {value2}']
        elif key in keys1:
            result += [f'  - {key}: {dict1[key]}']
        else:
            result += [f'  + {key}: {dict2[key]}']
    result += ['}']
    return '\n'.join(result)
