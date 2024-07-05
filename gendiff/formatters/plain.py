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
                               f" {to_str(value)}\n")
                else:
                    result += (f"Property '{make_key_view(key, curr_key)}'"
                               f" was added with value:"
                               f" {to_str(children)}\n")
            case 'updated':
                result += (f"Property"
                           f" '{make_key_view(key, curr_key)}' was updated."
                           f" From {to_str(updated_from)}"
                           f" to {to_str(updated_to)}\n")
            case 'nested':
                result += plain(children, make_key_view(key, curr_key)) + '\n'

    return result.rstrip()


def to_str(item):
    if isinstance(item, list):
        return '[complex value]'
    elif isinstance(item, str):
        return f"'{item}'"
    match item:
        case True:
            return 'true'
        case False:
            return 'false'
        case '':
            return ''
        case None:
            return 'null'
        case _:
            return f'{str(item)}'


def make_key_view(key, current_key):
    if current_key == '':
        current_key += key
    else:
        current_key += f'.{key}'
    return current_key
