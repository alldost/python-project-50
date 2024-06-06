from gendiff.parse import parse
from gendiff.formatters.stylish import stylish


def generate_diff(file1, file2, formater=None):
    dict1, dict2 = parse(file1, file2)
    diff_list = compare(dict1, dict2)

    if formater is None:
        formater = stylish

    #return diff_list
    return formater(diff_list)

def compare(dict1, dict2):
    difference = []
    keys = sorted(set(dict1) | set(dict2))

    def walk(dict_):
        result = []
        for key, value in dict_.items():
            entry_ = {'key': key}
            if not isinstance(value, dict):
                result.append({'key': key, 'value': value})
            else:
                entry_['children'] = walk(value)
                result.append(entry)
        return result

    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        entry = {'key': key}

        if isinstance(value1, dict) and isinstance(value2, dict):
            entry['status'] = 'unchanged'
            entry['children'] = compare(value1, value2)
            difference.append(entry)

        elif isinstance(value1, dict) and not isinstance(value2, dict):
            entry['status'] = 'removed'
            entry['children'] = walk(value1)
            difference.append(entry)

        elif not isinstance(value1, dict) and isinstance(value2, dict):
            entry['status'] = 'added'
            entry['children'] = walk(value2)
            difference.append(entry)

        else:
            if value1 == value2:
                difference.append({'key': key, 'status': 'unchanged', 'value': value1})
            else:
                if key in dict1:
                    difference.append({'key': key, 'status': 'removed', 'value': value1})
                if key in dict2:
                    difference.append({'key': key, 'status': 'added', 'value': value2})

    return difference
