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
	time = words[6]
	time = time.split(':')
	counts[time[0]] = counts.get(time[0], 0) + 1

lst = list()
for hour,count in counts.items():
	lst.append( (hour, count) )

lst.sort()

for hour, count in lst[0: ]:
	print hour, count
