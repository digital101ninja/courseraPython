#!/usr/bin/python

name = raw_input("Enter file:")
if len(name) < 1: name = "mbox-short.txt
handle = open(name, 'r')
senderList = dict()
for line in handle:
	eachLine = line.split()
	if(len(eachLine)>0):
		if(eachLine[0] == 'From'):
			name = eachLine[1]
			senderList[name] = senderList.get(name,0) + 1

maxValue = max(senderList.values())
print senderList.keys()[senderList.values().index(maxValue)],maxValue
	
  
	
