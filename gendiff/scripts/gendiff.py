#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def main():
       
    print(generate_diff('file1.json', 'file2.json'))


if __name__ == '__main__':
    main()
