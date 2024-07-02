import json
import yaml


def get_extension(file):
    if file.endswith(".json"):
        extension = 'json'
    elif file.endswith(".yaml") or file.endswith(".yml"):
        extension = 'yaml'

    with open(file, 'r') as f:
        data = f.read()

    return extension, data


def parse(extension, data):
    if extension == 'json':
        data_dict = json.loads(data)
    elif extension == 'yaml':
        data_dict = yaml.safe_load(data)

    return data_dict
