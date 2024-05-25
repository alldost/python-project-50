from gendiff.modules.parse_flat_files import parse_and_compare


def generate_diff(file1, file2):
    same, diff1, diff2 = parse_and_compare(file1, file2)

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
