from gendiff.modules.parse import parse


def generate_diff(file1, file2, formater=None):
    diff = dict()
    dict1, dict2 = parse(file1, file2)
    keys = sorted(set(dict1) | set(dict2))

    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = generate_diff(value1, value2)

        else:
            if value1 == value2:
                diff[key] = value1
            else:
                if key in dict1:
                    diff["- " + key] = value1
                if key in dict2:
                    diff["+ " + key] = value2

    if formater is None:
        formater = stylish

    # return diff
    return formater(diff)


def stylish(diff_dict, level=1):
    result = ''

    def stylish_level(value, current_level):
        level_result = ''

        if not isinstance(value, dict):
            return str(value)

        else:
            spaces_number = 4
            level_result += '{\n'

            for key, value in value.items():

                if key.startswith('+') or key.startswith('-'):
                    level_result += f'{(current_level * spaces_number - 2) * " "}{key}: '
                else:
                    level_result += f'{current_level * spaces_number * " "}{key}: '
                level_result += stylish_level(value, current_level + level) + '\n'
            level_result += f'{spaces_number * (current_level - level) * " "}' + '}'

        return level_result

    result += stylish_level(diff_dict, level)

    return result