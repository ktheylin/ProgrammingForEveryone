fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0

counts = dict()
for line in fh:
	line = line.rstrip()
	if line == '': continue
	words = line.split(' ')
	if words[0] != 'From': continue
	counts[words[2]] = counts.get(words[2], 0) + 1

print counts