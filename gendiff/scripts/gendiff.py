#!/usr/bin/env python3


import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', nargs=1, type=str, default=['plain'],
                        help='set format of output')
    parser.add_argument('first_file', nargs=1, type=str)
    parser.add_argument('second_file', nargs=1, type=str)
    # parser.add_argument('first_file', nargs=1, type=argparse.FileType('r'))
    # parser.add_argument('second_file', nargs=1, type=argparse.FileType('r'))
    args = parser.parse_args()
    print(args)
    print(f'FORMAT = {args.format[0]}')
    print(f'first_file = {args.first_file[0]}')
    print(f'second_file = {args.second_file[0]}')


if __name__ == '__main__':
    main()
