#!/usr/bin/python

import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter location:")
print "Retrieving",url
uh = urllib.urlopen(url)
data = uh.read()
print "Retrieved ", len(data), "characters"
print "Parsing"

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
counts = tree.findall(".//count")
print "count:", len(lst)
total = 0
for item in lst:
  print 'Name:',item.find('name').text
  print 'Count:',item.find('count').text
  total += int(item.find('count').text)
print "Total:", total

