fname = raw_input("Enter file name: ")
# if fname == '' : fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
	list = line.split(' ')
	for word in list:
		word = word.strip()
		if word not in lst:
			lst.append(word)
print sorted(lst)
