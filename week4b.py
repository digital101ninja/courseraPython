#!/usr/bin/python

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

countTime = int(raw_input('Enter Count - '))
positionGoal = int(raw_input('Enter Position - '))
url = raw_input('Enter URL- ')

# Retrieve all of the anchor tags
count = 0

for x in range(0, countTime):
  position = 0
  count = 0
  print 'X:',x
  print 'URL:',url
  match = re.search(r'known_by_(\w+).html',url)
  if(match):
	print match.group(0)
	print match.group(1)
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html)
  tags = soup('a')
  for tag in tags:
    count += 1
    newUrl = tag.get('href', None)
    if(count == positionGoal):
      print newUrl
      url = newUrl
      #url  = urllib.urlopen(newUrl).read()
      x += 1
      #break



