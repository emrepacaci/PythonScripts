#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description = 'handling errors when file do not exist')
parser.add_argument('filename', help='file to check')
parser.add_argument('line_number' , type=int, help='the number of line number to print')

args = parser.parse_args()

try:
    lines = open(args.filename, 'r').readlines()
    line = lines[args.line_number - 1 ]
except IndexError:
    print(f"Error: file {args.filename} doesn't have {args.line_number} lines.")
except IOError as err:
    print(f"Error:{err}")
else:
    print(line)





