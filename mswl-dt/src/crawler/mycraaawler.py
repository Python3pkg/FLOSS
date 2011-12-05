#!/usr/bin/python
# -*- coding: utf-8 -*-

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
from pymycraaawler import HtmlParser
from pymycraaawler import FileManager
from pymycraaawler import Settings
from pymycraaawler import CheckArguments
from pymycraaawler import ConnectionManager


'''
Created on 05/11/2011

@author: Cesar Valiente Gordo
@mail: cesar.valiente@gmail.com

Main class of the project (Python script to launch the application and use the 
different modules created in the pymycraaawler folder
'''
class MyCraaawler:
    
    #Objects to use
    _settings = None
    _connectionManager = None
    _checkArguments = None
    _htmlParser = None
    _fileManager = None
    
    #data
    _url = None
    
    def __init__(self):
        
        self._settings = Settings.Settings()
        
        #Check the arguments
        self._checkArguments = CheckArguments.CheckArguments()
        self._checkArguments.checkArguments()                
        
        #Works with the url
        self._connectionManager = ConnectionManager.ConnectionManager()
        self._connectionManager.readingRemoteFile(self._checkArguments.getUrl())        
                
        #Parses the raw html coded provided    
        self._htmlParser = HtmlParser.HtmlParser(self._connectionManager.getRawCode())        
        self._htmlParser.parseLinks()               
    
        self.checkFiles()

    """ Checks the files associated to the url """
    def checkFiles(self):
        
        #Gets the fileManager
        fileManager = FileManager.FileManager()        
        
        
        rawCode = self._connectionManager.getRawCode()     #Get the rawCode            
        links = self._htmlParser.getCorrectLinks()                  #Get the correct links        
        
        if (not fileManager.isSaved(self._settings.FILE_NAME + self._settings.HTML_FILE) and 
            not fileManager.isSaved(self._settings.FILE_NAME + self._settings.LINK_FILE)):
            
            fileManager.saveRawToDisk(rawCode)
            fileManager.saveLinksToDisk(links)
            
            print "Data saved in the disk"
        else:
            #TODO check links and show differences
            print "We already have the files"
            pass
            
        

def main():
    MyCraaawler()

if __name__ == '__main__':
    main()    
    
        
        