fname = raw_input('Enter a filename: ')
if len(fname) == 0:
	fname = 'words.txt'
try:
	fhand = open(fname)
except:
	print 'File not found:', fname
	exit()
for line in fhand:
	print line.rstrip().upper()
