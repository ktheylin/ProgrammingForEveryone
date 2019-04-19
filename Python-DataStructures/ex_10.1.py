fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

counts = dict()
tmp = dict()
for line in fh:
	line = line.strip()
	if line == '' : continue
	words = line.split(' ')
	if words[0] != 'From': continue
	from_addr = words[1]
	counts[from_addr] = counts.get(from_addr, 0) + 1

lst = list()
for from_addr,count in counts.items():
	lst.append( (count, from_addr) )

lst.sort(reverse=True)
count, from_addr = lst[0]
print from_addr, count