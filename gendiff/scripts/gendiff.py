#!/usr/bin/env python3


from gendiff.cli import get_args_after_launch
from gendiff import generate_diff


def main():
    diff = generate_diff(*get_args_after_launch())
    print(diff)


if __name__ == '__main__':
    main()


# v 0.9.1
#
# def main():
#     file_path1, file_path2, format_name = get_args_after_launch()
#     diff = generate_diff(file_path1, file_path2, format_name)
#     print(diff)
