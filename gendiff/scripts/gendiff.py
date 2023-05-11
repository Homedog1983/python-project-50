#!/usr/bin/env python3


import argparse
from gendiff import generate_diff


def get_cli_args() -> tuple:
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', nargs=1, type=str, default=['plain'],
                        help='set format of output')
    parser.add_argument('first_file', nargs=1, type=str)
    parser.add_argument('second_file', nargs=1, type=str)
    args = parser.parse_args()
    return args.format[0], args.first_file[0], args.second_file[0]


def main():
    _, file_path1, file_path2 = get_cli_args()
    diff = generate_diff(file_path1, file_path2)
    print(diff)


if __name__ == '__main__':
    main()
