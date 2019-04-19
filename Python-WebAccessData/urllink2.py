# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html'
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_168249.html'

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
