#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 21/09/2011

@author: Cesar Valiente Gordo

Practice 2: MSWL - Development and Tools '''

#imports
import sys
import string


class Prac2:
    
    FILE_NAME = "/etc/passwd"
     
    def __init__(self):
        userName = self.checkParams()
        if userName != None:
            self.checkUser(userName)
        else:
            print "Wrong params"

    ''' This function checks the parameters passed in the standard input '''
    def checkParams(self):
        if len(sys.argv) == 2:
            userName = sys.argv[1]
            return userName
        else:
            return None

    '''This function open the file, get the content and to place in a list '''
    def readLines(self):
        try:
            file = open(self.FILE_NAME, "r")
            linesList = file.readlines()
            file.close()
           
            return linesList
           
        except IOError:
            print "Error to open file"
            return None

    '''This function parse the list and write into the standard output the desired 
    information '''   
    def parseLines(self, linesList):
        
        DELIM = ":"
        try:
            myDictionary = {}            
            for item in linesList:
                list = string.split(item, DELIM)
                myDictionary[list[0]] = list[-1].strip()
                 
            return myDictionary                
        except Exception:
            print "Exception: " + Exception.message
            return None

    '''This function check the dictionay and the userName to get the userShell'''
    def checkUser(self, userName):
        linesList = self.readLines()
        myDictionary = self.parseLines(linesList)        
        if myDictionary != None:
            try:
                userShell = myDictionary[userName]
                print userName + " ->" + userShell
            except KeyError:
                print "The used user doesn't have any shell associated"

def main():
    Prac2()

if __name__ == '__main__':
    main()