fname = raw_input('Enter a filename: ')
if len(fname) == 0:
	fname = 'mbox-short.txt'
fhand = open(fname)
count = 0
for line in fhand:
	if not line.startswith("From ") : continue
	count = count + 1
	pieces = line.split()
	print pieces[1]
print 'There were', count, 'lines in the file with From as the first word'