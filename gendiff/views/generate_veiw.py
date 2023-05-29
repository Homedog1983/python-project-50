import gendiff.views.stylish as stylish
import gendiff.views.plain as plain
import gendiff.views.json_format as json_format


def get_view_from(tree, format_name):
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json_format
    }
    formatter = formats.get(format_name, stylish)
    return formatter.stringify(tree)
