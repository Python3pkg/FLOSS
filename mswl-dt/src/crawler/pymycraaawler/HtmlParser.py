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
Created on 06/11/2011

@author: Cesar Valiente Gordo
@mail: cesar.valiente@gmail.com

This class is used to parser an entire html document
'''

from BeautifulSoup import BeautifulSoup as Soup

class HtmlParser:
        
    _rawCode = None        
    
    """ Consturctor """
    def __init__ (self, rawCode):
        self._rawCode = rawCode
    
    
    """ Parse the links of the used raw code into a list """
    def parseLinks (self):
        
        if (self._rawCode != None):
            soupCode = Soup(self._rawCode)
            links = [link['href'] for link 
                     in soupCode.findAll('a') if link.has_key('href')]                                         
            print "Links: ", links
            
            for link in links:
                print link
                
            self.getRightLinks(links)
        
    def getRightLinks (self, links):
        
        print "----- parse links ----"
        
        if links != None or len(links)>0:
            for link in links:
                if (str(link).startswith("http://") or (str(link).startswith("https://"))):
                    print link
             
        
    
        


