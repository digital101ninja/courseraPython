import re 

#GOAL: print in ascending order of number of hours message is sent in. Practice use of tuples, and list comprehension
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
timeDict = dict()

for line in handle:
    if line.startswith("From "):
        result = re.search(r'(\d{2}):(\d{2}):(\d{2})',line)
        hour = result.group(1)
        timeDict[hour] = timeDict.get(hour,0) + 1

sortList = sorted([(k,v) for k,v in timeDict.items()])
for item in sortList:
    print item[0], item[1]
