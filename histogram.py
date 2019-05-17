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

for x in range(max(l)):
	ch = len(l) * [" "]
	for i in range(len(l)):
		if l[i] == max(l):
			ch[i] = "x"
			l[i] -= 1
	print(' '.join(ch))


