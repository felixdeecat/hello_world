# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:24:06 2016

@author: Thomas
"""

from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(open("Congressional Biographical Directory.htm"), "html")

#final_link = soup.p.a
#final_link.decompose()

f = csv.writer(open("Cleaned Congressional Biographical Directory.csv", "w"))
f.writerow(["Name", "Link"])

links = soup.find_all('a')

for link in links:
    names = link.contents[0]
    fullLink = link.get('href')
    
    f.writerow([names,fullLink])