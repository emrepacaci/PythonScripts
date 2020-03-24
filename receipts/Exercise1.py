#!/usr/bin/env python3.6
# name = input("What is your name")
# birthdate = input("What is your birthdate?")
# age = int(input("How old are you?"))

# print(f"{name} was born on {birthdate}" )
# print(f"Half of your age is {age/2}")


##def add_two(num):
##    return num + 2
##result = add_two(2)
##print(result)


# d



# working wih Environmental Variables 

# import os 

# stage = os.environ["STAGE"].upper()

# output = f"We're running in {stage}"
# if stage.startswith("PROD"):
#     output = "DANGER!!! - " + output
    
# print(output)

# Inreractin with files

# PRACTTISE- Using os package and Envrionment Variables
'''
# PROJECT-1: Prints the first ten digits of PI to the screen.
  Accepts an optional environment variable called DIGITS.
  If present, the script will print that many digits of PI instead of 10. 
'''
# from os import getenv
# from math import pi 

# digits = int(getenv("DIGITS") or 10)
# print("%.*f" % (digits,pi))


'''
 Parsing Command Line Parameters
 Using sys.argv is the simplest way to allow our scripts to accept positional arguments.
In the next video, we’ll explore a standard library package 
that will allow us to provide a more robust command line experience with help text, named arguments, and flags
'''
#  sys module and sys.argv attribute -- > most command use in daily, CI/CD pipeline. 

# import sys
# print(f"Postional arguments: {sys.argv[1:]} ")
# print(f"First argument: {sys.argv[1]}")


'''
Robust CLIs with 'argparse' - Part 1
'''
# # ! /usr/bin/env python 3
# import argparse
# # parser is instance of ArgumentParser class. Created without parameters. and using add_argument method.
# parser = argparse.ArgumentParser(description = 'Process some integers.')
# parser.add_argument('filename', help='the file to read')
# parser.add_argument('--limit', '-l', type = int, help='the number of lines to read')
# parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')
# args = parser.parse_args()
# print(args)


'''
Robust CLIs with 'argparse' - Part 2
READ ArgumentParser class documantation. lots of useful. 
'''
# reversing lines and then reverse each string in the line. 
# limiting 
# Added try, catch, else block. 
# import argparse

# parser = argparse.ArgumentParser(description = 'Process some integers.')
# parser.add_argument('filename', help='the file to read')
# parser.add_argument('--limit', '-l', type = int, help='the number of lines to read')
# parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')
# args = parser.parse_args()

# try:
#     f = open(args.filename)
#     limit = args.limit
# # except FileNotFoundError as err:
# #     print(f"Error:{err}")
# except: # except all possible errors. 
#     print(f"testing ")    
# else: # if error isn't happened then else block will be executed. 
#     with  f:
#         lines = f.readlines() # readlines method will give us list of lines. 
#         lines.reverse() # reverse contents of list, doesn't return new list just change contenst place in list 

#     if limit:
#         lines = lines[:limit]
    
#     for line in lines:
#         print(line.strip()[::-1]) # reverse the strings in each line 
# # finally:
# #     print('Finally') # happens every time. 


'''
Exit Statuses
When our reverse-file script receives a file that doesn’t exist,
 we show an error message, but we don’t set the exit status to 1 to be indicative of an error.
 Let’s use the sys.exit function to accomplish this:
 '''
# import argparse
# import sys

# parser = argparse.ArgumentParser(description = 'Process some integers.')
# parser.add_argument('filename', help='the file to read')
# parser.add_argument('--limit', '-l', type = int, help='the number of lines to read')
# parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')
# args = parser.parse_args()


# try:
#     f = open(args.filename)
#     limit = args.limit
# except FileNotFoundError as err:
#     print(f"Error:{err}")
#     sys.exit(1)
# else: # if error isn't happened then else block will be executed. 
#     with  f:
#         lines = f.readlines() # readlines method will give us list of lines. 
#         lines.reverse() # reverse contents of list, doesn't return new list just change contenst place in list 
#     if limit:
#         lines = lines[:limit]
    
#     for line in lines:
#         print(line.strip()[::-1]) # reverse the strings in each line 
'''
Execute Shell Commands from Python
'''

# import subprocess
# # proc variable is a CompleteProcess object: CompletedProcess(args=['ls', '-l'], returncode=0)

# proc = subprocess.run(['ls', '-l'])

# proc = subprocess.run(
# ...     ['ls', '-l'],
# ...     stdout=subprocess.PIPE,
# ...     stderr=subprocess.PIPE,
# ... )

'''
proc.stdout
b'total 20\ndrwxrwxr-x. 2 user user  54 Jan 28 15:36 bin\ndrwxr-xr-x. 2 user user
6 Jan  7  2015 Desktop\n-rw-rw-r--. 1 user user  44 Jan 26 22:16 new_xmen.txt\n-rw-rw-r--. 
1 user user  98 Jan 26 21:39 read_file.py\n-rw-rw-r--. 1 user user 431 Aug  6  2015 VNCHOWTO\n-rw-rw-r--. 1 user user  61 Jan 28 14:11 xmen_base.txt\n-rw-------. 1 user user  68 Mar 18  2016 xrdp-chansrv.log\n'
'''
# # Take a look at this string that is prefixed with a b character.
#  It is because it is a bytes object and not a string. 
#  The bytes type can only contain ASCII characters and 
#  won’t do anything special with escape sequences when printed. If we want to utilize this value as a string,
#   we need to explicitly convert it using the bytes.decode method.

# print(proc.stdout.decode()) // then we see as string. by decoding. 

# total 20
# drwxrwxr-x. 2 user user  54 Jan 28 15:36 bin
# drwxr-xr-x. 2 user user   6 Jan  7  2015 Desktop
# -rw-rw-r--. 1 user user  44 Jan 26 22:16 new_xmen.txt
# -rw-rw-r--. 1 user user  98 Jan 26 21:39 read_file.py
# -rw-rw-r--. 1 user user 431 Aug  6  2015 VNCHOWTO
# -rw-rw-r--. 1 user user  61 Jan 28 14:11 xmen_base.txt
# -rw-------. 1 user user  68 Mar 18  2016 xrdp-chansrv.log 

# Python 2 Compatible Functions
# If you’re interested in writing code with the subprocess module that will still work with Python 2,
#  then you cannot use the subprocess.run function because it’s only in Python 3. 
#  For this situation, you’ll want to look into using subprocess.call and subprocess.check_output.



'''
Advanced Iteration with List Comprehensions
We’ve talked about how often we’re likely to work with large amounts of data, 
and we often want to take a list and either:

Filter out items in that list
Modify every item in the list
For this, we can utilize “list comprehensions”.
'''
# To dig into list comprehensions, we’re going to write a script that takes a word 
# that then returns all of the values in the “words” file on our machine
#  that contain the word. Our first step will be writing the script using standard iteration, 
#  and then we’re going to refactor our script to utilize a list comprehension.

#! /usr/bin/env Python3

# import argparse

# parser = argparse.ArgumentParser(description = 'Search for words including partial word')
# parser.add_argument('snippet', help='partial (or complete) string to search for in words')

# args = parser.parse_args()

# snippet = args.snippet.lower()

# words =  open('/usr/share/dict/words').read().splitlines() # or readlines() then below need to use strip()
#                                                            # to ged rid of \mn charcter. 

# # matches=[]

# # for word in words:
# #     if snippet in word.lower():
# #         matches.append(word)

# # print(matches)

# # now utilize a list comprehension. 
# print([word for word in words if snippet in word.lower()])

'''
Our project dic comphension. 
https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
# '''
# raw = upload.file.read()
#     hashes = raw.splitlines()
#     result = {}
#     result.setdefault('resource',[])
#     result.setdefault('result',[])
#     result.setdefault('total',[])
#     result.setdefault('scan_date',[])
#     for hash in hashes:
#         response = getReport(hash.decode('utf-8)'))
#         if response:
#             result['resource'].append(response['resource'])
#             result['result'].append(response['result'])
#             result['total'].append(response["total"])
#             result['scan_date'].append(response['scan_date'])
#     headers=["hash_value (MD5 or Sha256)", "Fortinet detection name", "Number of engines detected", "Scan Dates"]
#     return tabulate(result, headers, tablefmt="html")


'''
To write our receipt reconciliation tool,   
we need to have some receipts to work with as we’re testing out our implementation.
We’re expecting receipts to be JSON files that contain some specific data 
and we’re going to write a script that will create some receipts for us.
'''

# import random
# import os
# import json

# count = int(os.getenv("FILE_COUNT") or 100)
# words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

# for identifier in range(count):
#     amount = random.uniform(1.0, 1000)
#     content = {
#         'topic': random.choice(words),
#         'value': "%.2f" % amount
#     }
#     with open(f'receipts/new/receipt-{identifier}.json', 'w') as f:
#         json.dump(content,f)#function to ensure that we’re writing out valid JSON
'''
Some of the most used utilities in Linux are mv, mkdir, cp, ls, and rm.
 Thankfully, we don’t need to utilize subprocess to access the same functionality of these utilities
because the standard library has us covered.
The remainder of our script is going to require us to do the following:
    Iterate over the receipts 
    Reading each receipt’s JSON
    Totaling the value of the receipts
    Moving each receipt file to the processed directory after we’re finished with it
'''
import os 
import glob
import shutil
import json

try:
    os.mkdir('receipts/processed')
except:
    print(f"'processed' directory already exits")

receipts = glob.glob('./new/receipt-[1-3]*.json')
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')[-1] # './new/receipt-1.json'.split('/') -- > ['.', 'new', 'receipt-1.json'][-1]
    destination = f"./processed/{name}" # we want to move exactly samefiles into process directory how?
    # we're gonna use shutil module move function. 
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")
    print(f"Receipt subtotal: $%.2f" % subtotal)