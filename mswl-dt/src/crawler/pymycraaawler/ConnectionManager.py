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


import urllib2
from Settings import Settings

'''
Created on 05/11/2011

@author: Cesar Valiente Gordo
@mail: cesar.valiente@gmail.com

This class has all methods to use in the connection with servers and urls
'''
class ConnectionManager:
    
    #Timeout to use un the remote file reading
    _TIMEOUT = 5000
    
    _rawCode = None
    
    """This function reads the website passed by parameter"""
    def readingRemoteFile(self, url):
        
        _opener = urllib2.build_opener()
        _opener.addheaders = [(Settings.USER_AGENT_TAG, Settings.USER_AGENT_CONTENT)]
        self._rawCode = _opener.open(url, None, self._TIMEOUT).read()
        
        #print "Raw code: ", raw_code
        
    
    def getRawCode (self):
        return self._rawCode
        
    

