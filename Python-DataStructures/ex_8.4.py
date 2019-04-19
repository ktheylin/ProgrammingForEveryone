fname = raw_input('Enter a filename: ')
if len(fname) == 0:
	fname = 'romeo.txt'
fhand = open(fname)
nline = []
for line in fhand:
	pieces = line.split()
	for word in pieces:
		if word not in nline:
			nline.append(word)
nline.sort()
print nline
