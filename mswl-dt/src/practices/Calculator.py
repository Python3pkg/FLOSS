#!/usr/bin/python
# -*- coding: utf-8 -*-

''' 
     Copyright 2011 Cesar Valiente Gordo
 
     This file is part of MSW - Development and Tools exercises.

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
Created on 21/09/2011

@author: Cesar Valiente Gordo

Practice 3 (Calculator): MSWL - Development and Tools '''

#imports
import sys


class Calculator:
    
    def __init__(self):
    
        (op1, operation, op2) = self.checkParams()
        if (op1 != None and operation != None and op2 != None):
            self.makingCalc(op1, operation, op2)
        else:
            print "Wrong parameters"
            
    
    ''' This function checks the parameters passed in the standard input '''
    def checkParams(self):
        try:            
            if len(sys.argv) == 4:                                                                  
                op1 = int(sys.argv[1])                                                        
                operation = sys.argv[2]                                        
                op2 = int(sys.argv[3])                            
                
                if operation == "+" or operation == "-" or operation == "/" or operation == "*":
                    return (op1, operation, op2)
            else:
                return (None, None, None)
        except ValueError:
            print "ValueError: " + ValueError.message
        except Exception:
            print "Exception: " + Exception.message
        else:
            return (None, None, None)

    '''This function calculates the operation '''
    def makingCalc (self, op1, operation, op2):
        if operation == "-":
            print (op1 - op2)
        elif operation == "+":
            print (op1 + op2)
        elif operation == "*":
            print (op1 * op2)
        elif operation == "/":
            print (op1 / op2)

def main():
    Calculator()

if __name__ == '__main__':
    main()