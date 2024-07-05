from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_ import to_json


def select_format(diff, formater):
    if formater == 'stylish':
        formater = stylish
    elif formater == 'plain':
        formater = plain
    elif formater == 'json':
        formater = to_json
    return formater(diff)
