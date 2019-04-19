import urllib
import xml.etree.ElementTree as ET

#fname = 'comments_42.xml'
fname = 'comments_168246.xml'
fhand = open(fname)
data = fhand.read().strip()
print data


#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml'
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_168246.xml'

#uh = urllib.urlopen(url)
#data = uh.read()

#print 'Retrieved',len(data),'characters'
#print "data =", data

commentinfo = ET.fromstring(data)
print "commentinfo =", commentinfo

#counts = commentinfo.findall('comments/comment/count')
#print 'counts =', counts

'''
for count in counts:
    print "count =", count
'''