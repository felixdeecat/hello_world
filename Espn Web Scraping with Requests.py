# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:50:27 2016

@author: Thomas
"""

from lxml import html
from lxml.html.soupparser import fromstring
import requests

PATH_URL = "http://espn.go.com/mlb/stats/batting"

page = requests.get(PATH_URL)
tree = html.fromstring(page.content)

#players = tree.xpath('/id/')
root = fromstring(tree)