import argparse


def get_args_after_launch() -> tuple:
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', type=str,
                        default='stylish', help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
