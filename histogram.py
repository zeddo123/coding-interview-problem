"""
This problem was asked by Square.

You are given a histogram consisting of rectangles of different heights.
These heights are represented in an input list, such that [1, 3, 2, 5]
corresponds to the following diagram:

	      x
	      x  
	  x   x
	  x x x
	x x x x
"""

l = [1, 5, 2, 5, 3, 4, 5, 7]

#first solution
for x in range(max(l)):
	ch = len(l) * [" "]
	for i in range(len(l)):
		if l[i] == max(l):
			ch[i] = "x"
			l[i] -= 1
	print(' '.join(ch))

#O(n) solution O(n²) print

l = [1, 5, 2, 5, 3, 4, 5, 7]
print('-'*len(l)*2)

matrix = []
max_value = max(l)

for x in l:
	matrix.append((max_value-x) * ' ' + x * '*')

for j in range(len(matrix[0])):
	for i in range(len(matrix)):
		print(matrix[i][j], end=' ')
	print(end='\n')


