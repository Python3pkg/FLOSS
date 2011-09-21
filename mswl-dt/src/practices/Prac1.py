#!/usr/bin/python
# -*- coding: utf-8 -*-

''' 
@author Cesar Valiente Gordo
@mail cesar.valiente@gmail.com

Practice 1: MSWL - Development and Tools '''

#Imports
import string


class Prac1:
    
    FILE_NAME = "/etc/passwd"
    
    ''' Init function '''
    def __init__(self):
        linesList = self.readLines()
        self.parseLines(linesList)
        
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
            for item in linesList:
                list = string.split(item, DELIM)
                print (list[0] + " -> " + list[-1].strip())
        
        except Exception:
            print "Exception: " + Exception.message
            

def main():
    Prac1()


if __name__ == '__main__':
    main()