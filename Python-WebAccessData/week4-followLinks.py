# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

tag_index = 17
loop = 7
count = 0

#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Asiya.html'

# Continue to read the next URL until loop counter has been met
while count < loop:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	
	# Get the index number of the tag
	tag = tags[tag_index]
#	print tag
	url = tag.get('href', None)
	print 'Retrieving:', url
	count = count + 1
