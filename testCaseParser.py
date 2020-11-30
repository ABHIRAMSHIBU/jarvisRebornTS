#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:29:29 2020

@author: Abhiram Shibu
Copyleft 2020 Project SSAL
"""

class TestCases:
    def __init__(self,file):
        import json
        self.json = json
        self.file=file
        self.refresh()
    def refresh(self):
        f=open(self.file,"r")
        d=self.json.loads(f.read())
        f.close()
        self.data=d
    def display(self):
        print(self.data)
    def getTestPatterns(self):
        return self.data["tp"]
    def getOffset(self):
        return self.data["offset"]