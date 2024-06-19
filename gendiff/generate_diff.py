from gendiff.parse import parse
from gendiff.formatters.stylish import stylish


def generate_diff(file1, file2, formater=None):
    dict1, dict2 = parse(file1, file2)
    diff_list = compare(dict1, dict2)

    if formater is None:
        formater = stylish

    return formater(diff_list)


def compare(dict1, dict2):
    difference = []
    keys = sorted(set(dict1) | set(dict2))

    for key in keys:
        if key in dict1 and key in dict2:
            value1 = dict1.get(key)
            value2 = dict2.get(key)
            if isinstance(value1, dict) and isinstance(value2, dict):
                difference.append({'key': key, 'status': 'nested',
                                   'children': compare(value1, value2)})
            elif value1 == value2:
                difference.append({'key': key, 'status': 'same',
                                   'value': value1})
            else:
                difference.append({'key': key, 'status': 'updated',
                                   'from': walk(value1), 'to': walk(value2)})

        elif key in dict1:
            value = dict1.get(key)
            if isinstance(value, dict):
                difference.append({'key': key, 'status': 'removed',
                                   'children': walk(value)})
            else:
                difference.append({'key': key, 'status': 'removed',
                                   'value': value})

        elif key in dict2:
            value = dict2.get(key)
            if isinstance(value, dict):
                difference.append({'key': key, 'status': 'added',
                                   'children': walk(value)})
            else:
                difference.append({'key': key, 'status': 'added',
                                   'value': value})

    return difference


def walk(item):
    if not isinstance(item, dict):
        return item
    result = []
    for key, value in item.items():
        dict_ = {'key': key}
        if not isinstance(value, dict):
            dict_['value'] = value
        else:
            dict_['children'] = walk(value)
        result.append(dict_)
    return result
