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
from pymycraaawler import Log

import difflib

'''
Created on 05/11/2011

@author: Cesar Valiente Gordo
@mail: cesar.valiente@gmail.com

Main class of the project (Python script to launch the application and use the 
different modules created in the pymycraaawler folder
'''
class MyCraaawler:
    
    _CLASS_NAME = "MyCraaawler"
    
    #Objects to use
    _settings = None
    _connectionManager = None
    _checkArguments = None
    _htmlParser = None
    _fileManager = None
    
    _log = None
    
    #data
    _url = None
    
    def __init__(self):
        
        self._settings = Settings.Settings()
        self._log = Log.Log()
        
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
        
        if (not fileManager.isSaved(self._settings.FILE_NAME_DEFAULT + self._settings.HTML_FILE) and 
            not fileManager.isSaved(self._settings.FILE_NAME_DEFAULT + self._settings.LINK_FILE)):
            
            fileManager.saveRawToDisk(rawCode)
            fileManager.saveLinksToDisk(links)
                        
        else:
            #TODO check links and show differences
            print "We already have the files"
            self.compareFiles(rawCode)
            
        
    """ Compare the two different url contents """    
    def compareFiles (self, newContent):
        
        fileManager = FileManager.FileManager()
        oldContent = fileManager.readFromDisk(self._settings.HTML_FILE)
        
        newContent = newContent.splitlines()
        oldContent = str(oldContent).splitlines()
        
        self._log.d(self._CLASS_NAME, "newContent: " + str(len(newContent)))
        self._log.d(self._CLASS_NAME, "oldContent: " + str(len(oldContent)))
        
        #Diff manual
        outFile = open(self._settings.CACHE_FOLDER + "results.txt", "w")
        x = 0
        for i in oldContent:
            if i != newContent[x]:
                outFile.write(i+" <> "+newContent[x])
            x += 1
 
        outFile.close()
        
        """ Diff Usando difflib
        d = difflib.Differ()
        diff = d.compare(oldContent, newContent)
        print '\n'.join(diff)
        """            
        

        
        
        
        
        

def main():
    MyCraaawler()

if __name__ == '__main__':
    main()    
    
        
        