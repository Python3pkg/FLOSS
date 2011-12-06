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

from Settings import Settings
from Log import Log
import os  

class FileManager:
        
    _CLASS_NAME = "FileManager"
    
    _log = None
    
    def __init__ (self):    
        self._log = Log()
    
    """ This function save to disk the given fileName and content """ 
    def saveRawToDisk (self, content, fileName=None):
                    
        if not os.path.exists(Settings.CACHE_FOLDER):
            os.makedirs(Settings.CACHE_FOLDER)
        
        if fileName == None:
            fileName = Settings.FILE_NAME_DEFAULT
            
        #self._log.d(self._CLASS_NAME, "content: " + str(content))
        fd = open (Settings.CACHE_FOLDER + fileName + Settings.HTML_FILE, 'w')
        fd.write(str(content)   )
        
        fd.close()
    
    """ This function save to disk the given fileName and content list """ 
    def saveLinksToDisk (self, contentList, fileName=None):

                    
            if not os.path.exists(Settings.CACHE_FOLDER):
                os.makedirs(Settings.CACHE_FOLDER)     
                
            if fileName == None:
                fileName = Settings.FILE_NAME_DEFAULT       
                                    
            fd = open (Settings.CACHE_FOLDER + fileName + Settings.LINK_FILE, 'w')
            
            if contentList != None:
                for link in contentList:                
                    fd.write(link + "\n")
            fd.close()

        
        
    """ this function reads a file and returns the content """    
    def readFromDisk (self, extension, fileName=None):
        
        try:
            if fileName == None:
                fileName = Settings.FILE_NAME_DEFAULT
            fd = open(Settings.CACHE_FOLDER + fileName + extension, 'r')
            content = fd.read()
            return content
        
        except IOError, ioe:
            Log().d(self._CLASS_NAME, ioe.message)
            return None
            
            
    """ Checks if the file was previously created or not """
    def isSaved (self, fileName):
        
        try:
            fd = open(Settings.CACHE_FOLDER + fileName, 'r')
            fd.close()                    
            if (fd != None):                
                return True
            else:
                return False            
        except IOError, ioe:
            return False
            
             
        

        
