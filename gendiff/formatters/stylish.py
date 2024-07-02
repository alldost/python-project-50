from gendiff.formatters.stringify import to_str


def stylish(nodes, level=1):
    result = ''
    spaces_number = 4
    result += '{\n'

    for node in nodes:
        key = node.get('key')
        status = node.get('status')
        updated_from = node.get('from')
        updated_to = node.get('to')

        if status in ['same', None, 'nested']:
            result += f'{level * spaces_number * " "}{key}: '
        elif status == 'removed':
            result += f'{(level * spaces_number - 2) * " "}- {key}: '
        elif status == 'added':
            result += f'{(level * spaces_number - 2) * " "}+ {key}: '
        elif status == 'updated':
            result += f'{(level * spaces_number - 2) * " "}- {key}: '
            if isinstance(updated_from, list):
                result += stylish(updated_from, level + 1) + '\n'
            else:
                result += to_str(updated_from) + '\n'
            result += f'{(level * spaces_number - 2) * " "}+ {key}: '
            if isinstance(updated_to, list):
                result += stylish(updated_to, level + 1) + '\n'
            else:
                result += to_str(updated_to) + '\n'

        children = node.get('children')
        value = node.get('value')
        if children:
            result += stylish(children, level + 1) + '\n'
        if value is not None:
            result += to_str(value)
            result = result.rstrip() + '\n'

    result += f'{spaces_number * (level - 1) * " "}' + '}'

    return result
