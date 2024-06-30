import json
import yaml


def parse(file):

    if file.endswith(".json"):
        with open(file) as f:
            file_to_dict = json.load(f)
            return file_to_dict

    elif file.endswith(".yaml") or file.endswith(".yml"):
        with open(file) as f:
            file_to_dict = yaml.safe_load(f)
            return file_to_dict

    else:
        raise ValueError("Unsupported file format")
