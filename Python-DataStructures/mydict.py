counts = dict()
names = ['csev','cwen','csev','zqian', 'cwen']
for name in names:
	if name not in counts:
		counts[name] = counts.get(name,0) + 1
print counts
