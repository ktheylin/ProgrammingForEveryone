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
	counts[words[1]] = counts.get(words[1], 0) + 1

bigcount = None
bigname = None
for name,count in counts.items():
	if bigcount is None or count > bigcount:
		bigname = name
		bigcount = count
		
print bigname, bigcount