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
    _settings = None
    _log = None
    
    
    """ Constructor """
    def __init__(self):
        
        #Initializes the objects to use in settings and log
        self._settings = Settings.Settings()
        self._log = Log.Log()
        
        #Check the arguments
        checkArguments = CheckArguments.CheckArguments()
        (url, deep) = checkArguments.checkArguments()                
        
        #Works with the url
        connectionManager = ConnectionManager.ConnectionManager()
        rawCode = connectionManager.readRemoteUrl(url)        
                
        #Processes raw html coded provided
        htmlParser = HtmlParser.HtmlParser()                              
        links = htmlParser.parseLinks(rawCode, url)                   
                
        self.visitLinks(links, deep, 0)

    """ Visits the links of the website which we get """
    def visitLinks (self, links, deep, index):                        
        
        #case base
        if (links == None):
            self._log.d(self._CLASS_NAME, "Return links == None")
            return
        elif (index > len(links) or deep < 0):
            self._log.d(self._CLASS_NAME, "Return index > links or deep < 0")
            return
        elif (index < len(links) and deep >= 0):
            self._log.d(self._CLASS_NAME, "1. Deep: " + str(deep) + "\tlink: " + str(links[index]))
            self.visitLinks(links, deep, (index+1))                        
        #recursive case
        else:                        
            connectionManager = ConnectionManager.ConnectionManager()
            htmlParser = HtmlParser.HtmlParser()
                        
            url = links[index]
            self._log.d(self._CLASS_NAME, "2.Deep: " + str(deep) + "\tlink: " + str(url))
            
            rawCode = connectionManager.readRemoteUrl(url)
            hostName = connectionManager.getHostName(url)
            newLinks = htmlParser.parseLinks(rawCode, hostName)
            
            self.visitLinks(newLinks, deep-1, 0)
            
            
            
        
        
        

        
        
        
        
        

def main():
    MyCraaawler()

if __name__ == '__main__':
    main()    
    
        
        