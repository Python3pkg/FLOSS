#!/usr/bin/python
# -*- coding: utf-8 -*-

''' 
     Copyright 2011 Cesar Valiente Gordo
 
     This file is part of MSWL - Development and Tools exercises.

    This file is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this file.  If not, see <http://www.gnu.org/licenses/>.
'''

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