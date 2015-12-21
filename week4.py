#!/usr/bin/python

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
spanTags = soup('span')
total = 0
count = 0
for spanTag in spanTags:
	print 'SPANTAG:',spanTag
	print 'Span Content:', spanTag.contents[0]
	total += int(spanTag.contents[0])
	count += 1
print 'total:',total
print 'count:',count
