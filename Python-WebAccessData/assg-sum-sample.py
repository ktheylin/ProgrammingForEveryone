import re

fname = raw_input('Enter a filename: ')
if len(fname) == 0:
	fname = 'regex_sum_sample.txt'
fhand = open(fname)
num_list = list()
num_line = list()
total = 0
count = 0
for line in fhand:
	if len(line) < 1:continue
	num_line = re.findall('([0-9]+)',line)
#	print "line = ", line
#	print "num_line = ", num_line
	if num_line:
		for s in num_line:
			num_list.append(float(s))
#	print "num_list = ", num_list
print "The sum of all the numbers is: ", sum(num_list)
print "The average of all the numbers is: ", sum(num_list) / len(num_list)