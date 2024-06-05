from gendiff.modules.parse import parse


def generate_diff(file1, file2, formater=None):
    diff = []
    dict1, dict2 = parse(file1, file2)
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
            entry['children'] = generate_diff(value1, value2)
            diff.append(entry)

        elif isinstance(value1, dict) and not isinstance(value2, dict):
            entry['status'] = 'removed'
            entry['children'] = walk(value1)
            diff.append(entry)

        elif not isinstance(value1, dict) and isinstance(value2, dict):
            entry['status'] = 'added'
            entry['children'] = walk(value2)
            diff.append(entry)

        else:
            if value1 == value2:
                diff.append({'key': key, 'status': 'unchanged', 'value': value1})
            else:
                if key in dict1:
                    diff.append({'key': key, 'status': 'removed', 'value': value1})
                if key in dict2:
                    diff.append({'key': key, 'status': 'added', 'value': value2})
    # return diff
    return stylish(diff)


def stylish(diff_list, level=1):
    result = ''

    def stylish_level(list_, current_level):
        level_result = ''

        # if not isinstance(list_, dict):
        #    return str(list_)

        spaces_number = 4

        if not isinstance(list_, list):
            level_result += str(list_)

        if isinstance(list_, list):

            level_result += '{\n'

            for item in list_:
                status = item.get('status')
                key = item.get('key')

                if status == 'unchanged' or status is None:
                    level_result += f'{current_level * spaces_number * " "}{key}: '
                elif status == 'removed':
                    level_result += f'{(current_level * spaces_number - 2) * " "}- {key}: '
                elif status == 'added':
                    level_result += f'{(current_level * spaces_number - 2) * " "}+ {key}: '

                if 'children' in item:
                    level_result += stylish_level(item['children'], current_level + level) + '\n'
                else:
                    level_result += str(item['value']) + '\n'
                # else:
                #    level_result += f'{current_level * spaces_number * " "}{item}'

            level_result += f'{spaces_number * (current_level - level) * " "}' + '}'
        return level_result

    result += stylish_level(diff_list, level)

    return result