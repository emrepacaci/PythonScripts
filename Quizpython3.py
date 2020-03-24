#!/usr/bin/env python
'''
It’s not uncommon for a process to run on a server and listen to a port.
Unfortunately, you sometimes don’t want that process to keep running, 
but all you know is the port that you want to free up. 
You’re going to write a script to make it easy to get rid of those pesky processes.

Write a script that does the following:

Takes a port_number as its only argument.
    Calls out to lsof to determine if there is a process listening on that port.
    If there is a process, kill the process and inform the user.
    If there is no process, print that there was no process running on that port.   

You can either use the kill command outside of Python or the os.kill(pid, 9) function.
Use this line of lsof to get the port information:
    lsof -n -i4TCP:PORT_NUMBER
'''
import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description = 'kill the running process listining on a given port')
parser.add_argument('port', type=int, help='the port number to search for')

port = parser.parse_args().port

try:
    result = subprocess.run(['lsof','-n', "-i4TCP:%s" % port],
                            stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)
except subprocess.CalledProcessError:
    print(f"No process listening on this {port}")
else:
    listening = None

    for line in result.stdout.splitlines():
        if 'LISTEN' in str(line):
            listening = line
            break
    
    if listening:
        # PID is the second column in the output
        pid = int(listening.decode().[0])
        os.kill(pid, 9)
        print(f"Killed process {pid}")
    else:
        print(f"No process listening on this {port}")
    