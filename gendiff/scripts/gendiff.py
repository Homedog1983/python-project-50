#!/usr/bin/env python3


from gendiff.cli import parse
from gendiff import generate_diff


def main():
    diff = generate_diff(*parse())
    print(diff)


if __name__ == '__main__':
    main()
