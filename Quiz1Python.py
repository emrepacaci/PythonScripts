#!/usr/bin/env Python3
import argparse

# def get_file_name(reprompt =False):
#     if reprompt:
#         print("Please enter a file name.")
#     file_name = input("Destination file name: ").strip()
#     return file_name

# file_name = get_file_name()
def get_file_name():
    parser = argparse.ArgumentParser(description = 'Quiz1')
    parser.add_argument('file_name', help='the file to write')
    
    args = parser.parse_args()
    return (args.file_name)


file_name = get_file_name()
print(f"Please enter your content. Entering an empty line will write the content to {file_name}")

with open(file_name, 'w') as f:
    lines= []

    while True:
        line = input()
        if line.strip():
            lines.append(line.strip())
        else:
            break;
    f.writelines(lines)
    print(f"lines written to {file_name}")
    