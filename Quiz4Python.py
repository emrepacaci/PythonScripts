#!/usr/bin/env python3

import argparse
import os
import requests
import sys


parser = argparse.ArgumentParser(description = 'Get the current weather information for your zipcode')
parser.add_argument('zip', help="zip/postal code t get weather for")
parser.add_argument('--country', default='us', help='country zip/postal belongs to, default is "us"')

args = parser.parse_args()

api_key = os.getenv("OWN_API_KEY")

if not api_key:
    print("Error:no 'OWN_API_KEY' provided")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

response = requests.get(url)

if response.status_code != 200:
    print(f"Error: Talking to weather provider:{response.status_code}")
    sys.exit(1)

print(response.json()) 
