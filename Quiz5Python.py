#!/usr/bin/env python3
import requests
import argparse
import sys


parser = argparse.ArgumentParser(description='making http request to the given URL and writing the contents of page out the destination')
parser.add_argument('URL', help="to store the content of")
parser.add_argument('filename', help='to store the content under')
parser.add_argument('--content-type', '-c', default='html', 
                                                choices=['html', 'json'],
                                                help='content-type URL being requested')
args = parser.parse_args()

respond = requests.get(args.URL)

if respond.status_code >= 400:
    print(f"Error: error code receipt {respond.status_code} ")
    sys.exit(1)

if args.content_type == 'json':
    content = json.dumps(respond.json())
else:
    content = respond.text


with open(args.filename, 'w', encoding = 'UTF-8') as f:
    f.write(content)
    print(f"Content written to {args.filename}")

