from gendiff.modules.parse import parse


def generate_diff(file1, file2):
    diff = dict()
    dict1, dict2 = parse(file1, file2)

    for key in set(dict1) | set(dict2):

        if dict1.get(key) == dict2.get(key):
            diff["  " + key] = dict1[key]

        else:
            if key in dict1:
                diff["- " + key] = dict1.get(key)
            if key in dict2:
                diff["+ " + key] = dict2.get(key)

    return stylish(diff)


def stylish(diff):
    result = []

    for key, value in diff.items():
        result.append(f'  {key}: {value}'.lower())

    result = sorted(result, key=lambda x: x[4:5])

    return '{\n' + '\n'.join(result) + '\n}'
