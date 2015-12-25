#!/usr/bin/python

import urllib
import json


#Sample web address for data: http://python-data.dr-chuck.net/comments_199687.json

while True:
	url= raw_input("Enter Location:")
	if len(url) < 1: break

	uh = urllib.urlopen(url)
	data = uh.read()
	print data
 
	info = json.loads(data)
	print 'User count:',len(info)
	commentList =  info['comments']
	sum = 0
	count = 0
	for item in commentList:
		count += 1
		sum += int(item['count'])
	print "Count:", count
	print "Sum:", sum		
