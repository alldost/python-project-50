#!/usr/bin/env python3

import argparse
from gendiff.formatters.plain import plain
from gendiff.formatters.json_ import to_json
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output')
    args = parser.parse_args()

    if args.format == 'plain':
        diff = generate_diff(args.first_file, args.second_file, plain)
    elif args.format == 'json':
        diff = generate_diff(args.first_file, args.second_file, to_json)
    else:
        diff = generate_diff(args.first_file, args.second_file)

    print(diff)


if __name__ == '__main__':
    main()
