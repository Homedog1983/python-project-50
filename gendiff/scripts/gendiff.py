#!/usr/bin/env python3


import argparse
from gendiff import generate_diff


def get_args_after_launch() -> tuple:
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', type=str,
                        default='stylish', help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    return args.format, args.first_file, args.second_file


def main():
    format_name, file_path1, file_path2 = get_args_after_launch()
    diff = generate_diff(file_path1, file_path2, format_name)
    print(diff)


if __name__ == '__main__':
    main()
