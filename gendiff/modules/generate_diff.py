from gendiff.modules.parse_json import parse_and_compare_json
from gendiff.modules.parse_yaml import parse_and_compare_yaml


def generate_diff(file1, file2):
    if file1.endswith(".json"):
        same, diff1, diff2 = parse_and_compare_json(file1, file2)

    if file1.endswith(".yaml") or file1.endswith(".yml"):
        same, diff1, diff2 = parse_and_compare_yaml(file1, file2)

    result = prepare_result(same, diff1, diff2)
    return result


def prepare_result(same, diff1, diff2):
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
