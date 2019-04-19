import urllib
import xml.etree.ElementTree as ET

tree = ET.parse('comments_42.xml')
#tree = ET.parse('comments_168246.xml')

#fhand = open(fname)
#data = fhand.read().strip()
root = tree.getroot()
#print root

for counts in root.findall('comments/comment/'):
	count = counts.find('count')
	print count
	

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml'
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_168246.xml'

#uh = urllib.urlopen(url)
#data = uh.read()

#print 'Retrieved',len(data),'characters'
#print "data =", data

#commentinfo = ET.fromstring(data)
#print "commentinfo =", commentinfo

#counts = commentinfo.findall('comments/comment/count')
#print 'counts =', counts

'''
for count in counts:
    print "count =", count
'''