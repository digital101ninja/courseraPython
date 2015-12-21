#!/usr/bin/python
import re

#fileIn = open("Sample.txt",'r')
#fileIn = open("regex_sum_42.txt",'r')
fileIn = open("regex_sum_199681.txt",'r')
total = 0
for line in fileIn:
	result = re.findall('[0-9]+',line)
	print result,len(result)
	print line
	if(len(result) > 0):
		for element in result:
			total+=int(element)

print "Total Sum:%d"%total
