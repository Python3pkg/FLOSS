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
from pymycraaawler import Settings
from pymycraaawler import CheckArguments
from pymycraaawler import ConnectionManager
from pymycraaawler import Log
import sys

'''
Created on 05/11/2011

@author: Cesar Valiente Gordo
@mail: cesar.valiente@gmail.com

Main class of the project (Python script to launch the application and use the 
different modules created in the pymycraaawler folder
'''
class MyCraaawler:
    
    _CLASS_NAME = "MyCraaawler"
    
    #Manager objects
    _connectionManager = None
    _htmlParser = None
    
    #Constants and log      
    _settings = None
    _log = None
    
    _deep = None
            
    def __init__(self):
        """ Constructor """
        #Initializes the objects to use in settings and log
        self._settings = Settings.Settings()
        self._log = Log.Log()
                
        """
        #Initialize the managers
        self._connectionManager = ConnectionManager.ConnectionManager()
        self._htmlParser = HtmlParser.HtmlParser()            
        
        #---------------------------------------------------------------#
        
        #Check the arguments
        checkArguments = CheckArguments.CheckArguments()
        (url, self._deep) = checkArguments.checkArguments()                
        
        #Works with the url        
        rawCode = self._connectionManager.readRemoteUrl(url)        
                
        #Processes raw html coded provided                                    
        links = self._htmlParser.parseLinks(rawCode, url)                   

        self.deep2 = self._deep
        
        self.visitLinksRecursively(links, self._deep, 0)        
        """
        
        #Alternative offline version
        deep = 3
        links = self.loadFile()
        
        self._log.d(self._CLASS_NAME, "links: " + str(links) + "\nlen(links): " + str(len(links)))
        
        self.visitLinksRecursively(links, deep, 0)
        


    def visitLinksRecursively (self, links, deep, index):
        """ Visits the links of the website which we get """
                                                                    
        self._log.d(self._CLASS_NAME, "Init. Index: " + str(index) + " deep: " 
                    + str(deep) + " len(list): " + str(len(links)))
        #case base
        if (index == len(links)):
            self._log.d(self._CLASS_NAME,  "Case1. deep:  " + str(deep) + " index: "
                         + str(index) + " len(list): " + str(len(links)))
            pass
                        
        elif (index < len(links) and deep == 0):            
            
            index = index +1
            url = links[index]
            self._log.d(self._CLASS_NAME,  "Case2. deep:  " + str(deep) + " index: " 
                        + str(index) + " len(list): " + str(len(links)) +  " -->\tlink: " + str(url))                                    
            #newLinks = self.getNewLinks(url)
            newLinks = self.loadFile()                                    
            self.visitLinksRecursively(newLinks, deep, index +1)
                                            
        elif (index < len(links) and deep > 0):                                 
                    
            url = links[index]
            self._log.d(self._CLASS_NAME,  "Case3. deep:  " + str(deep) + " index: "
                         + str(index) + " len(list): " + str(len(links)) +  " -->\tlink: " + str(url))            
            #newLinks = self.getNewLinks(url)
            newLinks = self.loadFile()        
            self.visitLinksRecursively(newLinks, deep-1, 0)
            
            self._log.d(self._CLASS_NAME, "visiting the new list. Deep: " + str(deep) 
                         + " len(list): " + str(len(links)) +  " Index: " + str(index+1))
            self.visitLinksRecursively(newLinks, deep, index+1)
                                    
                                                                                                            
    def getNewLinks (self, url):
        """ This function retrieves the new links of the website passed by param """        
        rawCode = self._connectionManager.readRemoteUrl(url)
        hostName = self._connectionManager.getHostName(url)
        newLinks = self._htmlParser.parseLinks(rawCode, hostName)
        
        return newLinks
                        
                        
    #-----------------    To use just for offline mode    ---------------------------#
    def loadFile (self):                
        fd = open("pymycraaawler/links.txt", "r")
        content = fd.readlines()
        fd.close()                  
        
        newLinks = []
        for line in content:
            newLinks.append(line)
            
        return newLinks
               
            
            
        
        
        

        
        
        
        
        

def main():
    MyCraaawler()

if __name__ == '__main__':
    main()    
    
        
        