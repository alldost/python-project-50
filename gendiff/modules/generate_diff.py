import json


def generate_diff(file1, file2):
    same = dict()
    diff1 = dict()
    diff2 = dict()
    with open(file1) as f1, open(file2) as f2:
        dict1 = json.load(f1)
        dict2 = json.load(f2)
        for key in set(dict1) | set(dict2):
            if dict1.get(key) == dict2.get(key):
                same[key] = dict1[key]
            else:
                diff1[key] = dict1.get(key)
                diff2[key] = dict2.get(key)

    result = prepare_result(same, diff1, diff2)
    return result


def prepare_result(same, diff1, diff2):
    result = []
    for key in same:
        same_to_str = f'  {key}: {same[key]}'
        result.append(same_to_str)
    for key in diff1:
        if diff1[key] is not None:
            diff1_to_str = f'- {key}: {diff1[key]}'
            result.append(diff1_to_str)
    for key in diff2:
        if diff2[key] is not None:
            diif2_to_str = f'+ {key}: {diff2[key]}'
            result.append(diif2_to_str)
    result = sorted(result, key=lambda x: x[2:3])
    return '{\n' + '\n'.join(result) + '\n}'
