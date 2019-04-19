import json
import urllib

total = 0
characters = 0
count = 0

url = 'http://python-data.dr-chuck.net/comments_42.json'
#url = 'http://python-data.dr-chuck.net/comments_168250.json'

uh = urllib.urlopen(url)
data = uh.read()

#fhand = open('comments_42.json')
#data = fhand.read()

info = json.loads(data)
characters = len(data)
count = len(info['comments'])
 
for item in info['comments']:
	total = total + item['count']
	
print 'Retrieved', characters, 'characters'
print 'Count:', count
print 'Sum:', total