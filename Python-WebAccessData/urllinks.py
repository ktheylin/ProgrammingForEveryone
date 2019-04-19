# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

inner_loop = 3
count = 0
#url = raw_input('Enter - ')
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Asiya.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	url = tag.get('href', None)
	while count < outer_loop
	count = count + 1
	if count == inner_loop:
		html = urllib.urlopen(url).read()
		#print url
		continue