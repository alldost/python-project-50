from gendiff.parse import get_extension, parse
from gendiff.tree_generator import make_tree
from gendiff.formatters.format_selector import select_format


def generate_diff(file1, file2, formater='stylish'):
    dict1 = parse(*get_extension(file1))
    dict2 = parse(*get_extension(file2))
    diff_list = make_tree(dict1, dict2)
    return select_format(diff_list, formater)
