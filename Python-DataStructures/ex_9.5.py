fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0

domains = dict()
for line in fh:
	line = line.rstrip()
	if line == '': continue
	words = line.split(' ')
	if words[0] != 'From': continue
	pieces = words[1].split('@')
	domains[pieces[1]] = domains.get(pieces[1], 0) + 1

print domains