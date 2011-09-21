#!/usr/bin/python
# -*- coding: utf-8 -*-

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

    '''This functions calculates the operation '''
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