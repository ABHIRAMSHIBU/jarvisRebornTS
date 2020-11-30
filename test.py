#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:33:59 2020

@author: Abhiram Shibu
@author: Preet Patel
Copyleft 2020 Project SSAL
"""
class test:
    def __init__(self,ssalhw,tp,offset):
        self.ssalhw=ssalhw
        self.tp=tp
        self.offset=offset
    def run(self):
        testpass = True
        for i in self.tp:
            if(self.testSequence(i)==False):
                testpass=False
        return testpass
    def testSequence(self,sequence):
        from time import sleep
        testpass = True
        for i in range(self.offset,len(sequence)+self.offset):
            sleep(0.07)
            self.ssalhw.sendCRLF(str(i)+" "+str(sequence[i-self.offset]))
            response=self.ssalhw.readLine()
            if(response.strip()!=(str(i)+" "+str(sequence[i-self.offset]))):
                print("Expected ",str(i)+" "+str(sequence[i-self.offset]), " Got ",response.strip(),"Pattern",sequence, "Iteration",i-self.offset)
                testpass=False
            else:
                print("Passed ",str(i)+" "+str(sequence[i-self.offset]), " Got ",response.strip(),"Pattern",sequence, "Iteration",i-self.offset)
        return testpass