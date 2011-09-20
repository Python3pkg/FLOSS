#!usr/bin/python
#-*- coding: iso-utf-8 -*-

''' 
@author Cesar Valiente Gordo
@mail cesar.valiente@gmail.com

Practice 1: MSWL - Development and Tools '''

#Imports
import sys



class Practice1:
    
    fileName = "/etc/passwd"
    
    
    ''' Init function '''
    def __init__(self):
        self.readFileName()
        
        
    ''' This function reads the filename and show the content on the output '''
    def writeOutput(self):
        linesList = self.readLines()
        
        
    def readLines(self):
        try:
            file = open(self.fileName, "r")
            linesList = file.readlines()
            file.close()
            
            return linesList
            
        except IOError:
            print "Error to open file"
            return None
        
    def parseLines(self, linesList):
        
        try:
            for item in linesList:
                
        
        except Exception:
            print "Controlled exception"
            
            
            
    
    
def main():
    practice1 = Practice1()


if __name__ == '__main__':
    main()