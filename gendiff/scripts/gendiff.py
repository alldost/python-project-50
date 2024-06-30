#!/usr/bin/env python3

import argparse
from gendiff.generate_diff import generate_diff


def arguments_parse():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output')
    return parser.parse_args()


def main():
    args = arguments_parse()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
