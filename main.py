#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:04:10 2020

@author: Abhiram Shibu
Copyleft ProjectSSAL
"""

from testTimeStability import TimeStability
from sys import argv
host=None
port=None
if(len(argv)!=0):
    for i in range(len(argv)):
        if(argv[i]=="--host" or argv[i]=="-h"):
            try:
                host=argv[i+1]
                # check ipv4/ipv6 address here
            except:
                print("Host not detected or syntax incorrect")
                exit(-1)
        elif(argv[i]=="--port" or argv[i]=="-p"):
            port=argv[i+1]
            try:
                port=int(port)
                if(port>65535 or port<2):
                    print("Port out of range")
                    exit(-1)
            except:
                print("Port not detected or syntax incorrect")
                exit(-1)
print("Detected host as ",host,",detected port as ",port)
if(host==None or port==None):
    print("Host and port needed to function")
    exit(1)
ts=TimeStability(host, port)
ts.run()