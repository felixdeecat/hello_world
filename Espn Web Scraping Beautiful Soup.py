# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:38:24 2016

@author: Thomas
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
from lxml.html.soupparser import fromstring

PATH_URL = "http://espn.go.com/mlb/stats/batting"


html = urlopen(PATH_URL).read()
soup = BeautifulSoup(html, "lxml")

root = fromstring(soup)

#mlbLeaders = []
#mlbLeaders = soup.find_all("div", "span-6")
#
#
#print mlbLeaders[2]

#print list(mlbLeaders[2])[1].find_all(text = re.compile('id'))
