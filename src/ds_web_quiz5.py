# coding: utf-8
import lxml.html
from lxml.cssselect import CSSSelector
from bs4 import BeautifulSoup
import requests
r = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')
bs = BeautifulSoup(r.text)
nodes = bs.find_all('td', class_='pad10')
for node in nodes:
    print node.p.a.text
    print "----------"