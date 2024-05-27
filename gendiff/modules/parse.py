import json
import yaml


def parse(file1, file2):

    if file1.endswith(".json"):
        with open(file1) as f1, open(file2) as f2:
            dict1 = json.load(f1)
            dict2 = json.load(f2)
            return dict1, dict2

    elif file1.endswith(".yaml") or file1.endswith(".yml"):
        with open(file1) as f1, open(file2) as f2:
            dict1 = yaml.safe_load(f1)
            dict2 = yaml.safe_load(f2)
            return dict1, dict2

    else:
        raise ValueError("Unsupported file format")
