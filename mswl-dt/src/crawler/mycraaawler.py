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

from pymycraaawler import ClassWiring
from pymycraaawler import HtmlParser
from lxml.doctestcompare import _html_parser


'''
Created on 05/11/2011

@author: Cesar Valiente Gordo
@mail: cesar.valiente@gmail.com

Main class of the project (Python script to launch the application and use the 
different modules created in the pymycraaawler folder
'''
class MyCraaawler:
    
    #Objects to use
    _connectionManager = None
    _checkArguments = None
    _htmlParser = None
    
    def __init__(self):
        
        #Check the arguments
        self._checkArguments = ClassWiring.ClassWiring().getCheckArguments()
        self._checkArguments.checkArguments()                
        
        #Works with the url
        self._connectionManager = ClassWiring.ClassWiring().getConnectionManager()
        self._connectionManager.readingRemoteFile(self._checkArguments.getUrl())
                
        self._htmlParser = HtmlParser.HtmlParser(self._connectionManager.getRawCode())
        self._htmlParser.parseLinks()        


def main():
    MyCraaawler()

if __name__ == '__main__':
    main()    
    
        
        