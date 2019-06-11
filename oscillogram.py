def crest(max_point):
	# creating the histogram liste [1..max_point..1]
	l = [i for i in range(1,max_point+1)]
	l += l[::-1][1::]

	crest_top = []
	for x in range(max_point):
		ch = len(l) * [' ']
		maximum = max(l)

		for i in range(len(l)):
			if l[i] == maximum:
				ch[i] = '\\'
				l[i] -= 1

		crest_top.append(' '.join(ch))

	crest_buttom = [' '.join(len(l) * [' ']) for x in range(max_point)]
	
	return crest_top + crest_buttom

period = 3
max_value = 3
for p,n in zip(crest(max_value),crest(max_value)[::-1]):
	for i in range(period):
		print(p,n,end='')
	print()