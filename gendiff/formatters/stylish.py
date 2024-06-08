def stylish(nodes, level):
    result = ''
    spaces_number = 4
    if level == 1:
        result += '{\n'
    else:
        result += ' {\n'

    for node in nodes:
        key = node.get('key')
        status = node.get('status')

        match status:
            case 'same' | None:
                result += f'{level * spaces_number * " "}{key}:'
            case 'removed':
                result += f'{(level * spaces_number - 2) * " "}- {key}:'
            case 'added':
                result += f'{(level * spaces_number - 2) * " "}+ {key}:'

        children = node.get('children')
        if children:
            result += stylish(children, level + 1) + '\n'
        else:
            result += change_format(node['value']) + '\n'

    result += f'{spaces_number * (level - 1) * " "}' + '}'

    return result


def change_format(value):
    match value:
        case True:
            return ' true'
        case False:
            return ' false'
        case '':
            return ''
        case None:
            return ' null'
        case _:
            return f' {str(value)}'
