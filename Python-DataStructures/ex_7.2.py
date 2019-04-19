fname = raw_input('Enter a filename: ')
if len(fname) == 0:
	fname = 'mbox-short.txt'
try:
	fhand = open(fname)
except:
	print 'File not found:', fname
	exit()

total = 0
count = 0
for line in fhand:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	count = count + 1
	pieces = line.split(':')
	fnum = float(pieces[1])
	total = total + fnum
	avg = total / count
print 'Average spam confidence:', avg