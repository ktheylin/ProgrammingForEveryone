# Use the file name mbox-short.txt as the file name
total = 0
count = 0
fname = raw_input("Enter file name: ")
fh = open(fname)
#fh = open("mbox-short.txt")
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	pieces = line.split(":")
	num = pieces[1].rstrip()
	num = float(num)
	total = total + num
	count = count + 1
#	print num
#	print line
print "Average spam confidence:", total / count
