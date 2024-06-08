from gendiff.parse import parse
from gendiff.formatters.stylish import stylish


def generate_diff(file1, file2, formater=None):
    dict1, dict2 = parse(file1, file2)
    diff_list = compare(dict1, dict2)

    if formater is None:
        formater = stylish

    return formater(diff_list, 1)


def compare(dict1, dict2):
    difference = []
    keys = sorted(set(dict1) | set(dict2))

    for key in keys:
        if key in dict1 and key in dict2:
            value1 = dict1.get(key)
            value2 = dict2.get(key)
            if isinstance(value1, dict) and isinstance(value2, dict):
                difference.append({'key': key, 'status': 'same',
                                   'children': compare(value1, value2)})
            elif isinstance(value1, dict):
                difference.append({'key': key, 'status': 'removed',
                                   'children': walk(value1)})
                difference.append({'key': key, 'status': 'added',
                                   'value': value2})
            elif isinstance(value2, dict):
                difference.append({'key': key, 'status': 'removed',
                                   'value': value1})
                difference.append({'key': key, 'status': 'added',
                                   'children': walk(value2)})
            elif value1 == value2:
                difference.append({'key': key, 'status': 'same',
                                   'value': value1})
            else:
                difference.append({'key': key, 'status': 'removed',
                                   'value': value1})
                difference.append({'key': key, 'status': 'added',
                                   'value': value2})

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


def walk(dict_):
    result = []
    for key, value in dict_.items():
        entry_ = {'key': key}
        if not isinstance(value, dict):
            result.append({'key': key, 'value': value})
        else:
            entry_['children'] = walk(value)
            result.append(entry_)
    return result
