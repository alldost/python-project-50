#!/usr/bin/env python3

from gendiff.argparser import arguments_parse
from gendiff.generate_diff import generate_diff


def main():
    args = arguments_parse()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
