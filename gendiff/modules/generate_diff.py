from gendiff.modules.parse import parse


def generate_diff(file1, file2):
    same = dict()
    diff1 = dict()
    diff2 = dict()
    dict1, dict2 = parse(file1, file2)

    for key in set(dict1) | set(dict2):

        if dict1.get(key) == dict2.get(key):
            same[key] = dict1[key]

        else:
            diff1[key] = dict1.get(key)
            diff2[key] = dict2.get(key)

    return stylish(same, diff1, diff2)


def stylish(same, diff1, diff2):
    result = []

    for key, value in same.items():
        result.append(f'    {key}: {value}'.lower())

    for key, value in diff1.items():
        if value is not None:
            result.append(f'  - {key}: {value}'.lower())

    for key, value in diff2.items():
        if value is not None:
            result.append(f'  + {key}: {value}'.lower())

    result = sorted(result, key=lambda x: x[4:5])

    return '{\n' + '\n'.join(result) + '\n}'
