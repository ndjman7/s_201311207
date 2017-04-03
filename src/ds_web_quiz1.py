# coding: utf-8
import re
import requests
response = requests.get('http://python.org/')
html = response.text
p = re.compile('href="(http://.*?)"')
nodes = p.findall(html)
print "http url의 개수는",len(nodes),'개'
for index, node in enumerate(nodes):
    print index+1,'번',node