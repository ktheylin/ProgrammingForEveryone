import json
import urllib

total = 0
characters = 0
count = 0

fhand = open('comments_42.json')
#fhand = open('comments_168250.json')

data = fhand.read()
info = json.loads(data)
characters = len(data)
count = len(info['comments'])

for item in info['comments']:
	#print item
    #print 'Name', item['name']
    #print 'Count', item['count']
	total = total + item['count']
	
print 'Retrieved', characters, 'characters'
print 'Count:', count
print 'Sum:', total

