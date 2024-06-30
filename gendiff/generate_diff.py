from gendiff.parse import parse
from gendiff.tree_generator import make_tree
from gendiff.formatters.format_selector import select_format


def generate_diff(file1, file2, formater=None):
    dict1 = parse(file1)
    dict2 = parse(file2)
    diff_list = make_tree(dict1, dict2)
    format = select_format(formater)
    return format(diff_list)
