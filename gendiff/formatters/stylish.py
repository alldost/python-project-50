

def stylish(diff_list, level=1):
    result = ''

    def stylish_level(curr_list, curr_level):
       level_result = ''
       spaces_number = 4
       level_result += '{\n'

       for dict in curr_list:
           children = dict.get('children')

           if children:
               level_result += stylish_level(children, curr_level + level)

           key = dict.get('key')
           status = dict.get('status')
           value = dict.get('value')

           match status:
               case 'unchanged' | None:
                   level_result += f'{curr_level * spaces_number * " "}{key}: '
               case 'removed':
                   level_result += f'{(curr_level * spaces_number - 2) * " "}- {key}: '
               case 'added':
                   level_result += f'{(curr_level * spaces_number - 2) * " "}+ {key}: '

           level_result += change_format(value) + '\n'

       level_result += f'{spaces_number * (curr_level - level) * " "}' + '}'

       return level_result

    result += stylish_level(diff_list, level)
    return result


def change_format(value):
    match value:
        case True:
            return 'true'
        case False:
            return 'false'
        #case '':
        #    return None
        case None:
            return 'null'
        case _:
            return str(value)
