import json


def to_json(nodes):
    result = json.dumps(nodes, indent=4)
    return result
