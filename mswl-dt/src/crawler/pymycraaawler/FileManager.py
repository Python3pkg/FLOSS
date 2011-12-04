''' 
     Copyright 2011 Cesar Valiente Gordo
 
     This file is part of MSWL - Development and Tools WebCrawler exercise.

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
Created on 07/11/2011

@author: Cesar Valiente Gordo
@mail: cesar.valiente@gmail.com

This class has the functionality regarding i/o
'''


class FileManager:
    
    def __init__ (self):
        pass
    
    """ This function save to disk the given fileName and content """ 
    def saveToDisk (self, fileName, content):

        try:
            fd = open (fileName, 'w')
            fd.write (content)
            fd.close()

        except IOError:
            print "Exception ", IOError.message
        
    """ this function reads a file and returns the content """    
    def readFromDisk (self, fileName):
        
        try:
            fd = open(fileName, 'r')
            content = fd.read()
            return content
        
        except IOError:
            print "Exception ", IOError.message

        
