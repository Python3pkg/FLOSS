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


from ConnectionManager import ConnectionManager
from CheckArguments import CheckArguments
from FileManager import FileManager


'''
Created on 05/11/2011

@author: Cesar Valiente Gordo
@mail: cesar.valiente@gmail.com

This class following the singleton pattern to get just one instance of the 
different objects used along the application
'''
class ClassWiring:
  
    #Objects  
    _connectionManager = None
    _checkArguments = None
    _fileManager = None
    
    """ This function creates the object ConnectionManager if doesn't exist and return it """
    def getConnectionManager (self):
        
        if self._connectionManager == None:
            self._connectionManager = ConnectionManager()
        
        return self._connectionManager
    
    
    """ This function creates the object CheckArguments if doesn't exist and return it """
    def getCheckArguments (self):
        
        if self._checkArguments == None:
            self._checkArguments = CheckArguments()
            
        return self._checkArguments 
    
    """ Creates if not exists the FileManager object to use along the application """
    def getFileManager (self):
        
        if self._fileManager == None:
            self._fileManager = FileManager()
        
        return self._fileManager
            