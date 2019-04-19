import re

fname = raw_input('Enter a filename: ')
if len(fname) == 0:
	fname = 'regex_sum_actual.txt'
fhand = open(fname)
num_list = list()
num_line = list()
total = 0
count = 0
for line in fhand:
	if len(line) < 1:continue
	num_line = re.findall('([0-9]+)',line)
	if num_line:
		for s in num_line:
			num_list.append(int(s))
print sum(num_list)
