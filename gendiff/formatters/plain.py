from gendiff.formatters.stringify import to_str


def plain(nodes, curr_key=''):
    result = ''

    for node in nodes:
        key = node.get('key')
        status = node.get('status')
        value = node.get('value')
        children = node.get('children')
        updated_from = node.get('from')
        updated_to = node.get('to')

        match status:
            case 'removed':
                result += (f"Property '{make_key_view(key, curr_key)}'"
                           f" was removed\n")
            case 'added':
                if value is not None:
                    result += (f"Property '{make_key_view(key, curr_key)}'"
                               f" was added with value:"
                               f" {check_and_format(value)}\n")
                else:
                    result += (f"Property '{make_key_view(key, curr_key)}'"
                               f" was added with value:"
                               f" {check_and_format(children)}\n")
            case 'updated':
                result += (f"Property"
                           f" '{make_key_view(key, curr_key)}' was updated."
                           f" From {check_and_format(updated_from)}"
                           f" to {check_and_format(updated_to)}\n")
            case 'nested':
                result += plain(children, make_key_view(key, curr_key)) + '\n'

    return result.rstrip()


def check_and_format(item):
    if isinstance(item, list):
        return '[complex value]'
    elif isinstance(item, dict):
        return to_str(item['value'])
    elif item is None:
        return 'null'
    elif isinstance(item, str):
        return f"'{to_str(item)}'"
    else:
        return to_str(item)


def make_key_view(key, current_key):
    if current_key == '':
        current_key += key
    else:
        current_key += f'.{key}'
    return current_key
