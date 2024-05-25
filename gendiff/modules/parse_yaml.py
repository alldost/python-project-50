import yaml


def parse_and_compare_yaml(file1, file2):
    same = dict()
    diff1 = dict()
    diff2 = dict()

    with open(file1) as f1, open(file2) as f2:
        dict1 = yaml.safe_load(f1)
        dict2 = yaml.safe_load(f2)

    for key in set(dict1) | set(dict2):

        if dict1.get(key) == dict2.get(key):
            same[key] = dict1[key]

        else:
            diff1[key] = dict1.get(key)
            diff2[key] = dict2.get(key)

    return same, diff1, diff2
