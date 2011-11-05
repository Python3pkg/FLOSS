'''
Created on 25/09/2011

@author: cesar
'''

from setuptools import setup, find_packages

setup (name = "MyCraaawler",
    version = "0.1",
    packages = find_packages(),
    scripts = ['mycraaawler'],
    install_requires = ['BeautifulSoup'],
    package_data = {'pymycraaawler':[''],},
    author = "Cesar Valiente Gordo",
    author_email = "cesar.valiente@gmail.com",
    description = "WebCrawler for the  Development & Tools subject of the M.Sc. on Free Software",
    license = "GNU GPLv3",
    keywords = "webcrawler",
    url = "",
    long_description = "",
    download_url = "", )

