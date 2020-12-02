#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:12:06 2020

@author: abhiram
"""

class TimeStability:
    def __init__(self,ip,port,testData="testCase.json",timeout=0.5,initime=60):
        from test import test
        from testCaseParser import TestCases
        from telnetClient import telnet
        self.ip = ip 
        self.port = port
        self.initime = initime
        tc=TestCases(testData)
        self.testData = tc.getTestPatterns()
        self.testOffset = tc.getOffset()
        self.tn = telnet(ip, port)
        self.currentTest = test(self.tn,self.testData,self.testOffset)
    def run(self):
        from time import sleep
        currtime=self.initime
        while(currtime<=(7*24*60)):
            try:
                if(self.currentTest.run()==False):
                    print("Test failure, test duration ",currtime/2)
                print("Waiting",currtime,"seconds")
                sleep(currtime)
                currtime*=2
            except EOFError:
                print("Connection got closed by test hardware, reconnecting")
                self.tn.reconnect()
        self.tn.close()