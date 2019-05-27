"""
This problem was asked by LinkedIn.

You are given a string consisting of the letters x and y,
such as xyxxxyxyy.

In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times 
you would need to apply this operation to ensure that all x's come before all y's.

In the preceding example,
it suffices to flip the second and sixth characters, so you should return 2.
"""

def flip(l, position):
	try:
		l[position] = 'x' if l[position] == 'y' else 'y'
	except IndexError:
		print('IndexError')
	
	return l

def number_of_times(string):
	tmp = list(string)
	i = 0
	b = True

	first_y = tmp.index('y')
	last_x = len(tmp) - 1 - tmp[::-1].index('x') 
	
	while first_y < last_x and b:
		tmp = flip(tmp, first_y)
		i += 1
		try:
			first_y = tmp.index('y')
			last_x = len(tmp) - 1 - tmp[::-1].index('x')
		except ValueError:
			b = False

	return (i, ''.join(tmp))

string = 'xyxxxyxyy'
print(string, number_of_times(string), end='\n\n')

string = 'yxyxxyxyy'
print(string, number_of_times(string))


