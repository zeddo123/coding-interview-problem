"""This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""
def is_strobogrammatic(n):
	string = str(n)
	return ''.join([i if not i in ('6', '9') else '6' if i == '9' else '9' for i in string[::-1]]) == string

def last_number(N):
	s = 0
	for i in range(N):
		s += 10**i
	return s

N = 5

a = 10**(N-1)
b = 9*last_number(N)

print('found ',len([i for i in range(a,b) if is_strobogrammatic(i)]))