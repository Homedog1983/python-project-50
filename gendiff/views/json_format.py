from json import dumps


def stringify(tree):
    return dumps(tree, indent=4)
