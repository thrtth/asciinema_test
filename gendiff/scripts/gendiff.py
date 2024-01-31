#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    
    print(generate_diff('file1.json', 'file2.json'))


if __name__ == '__main__':
    main()
