"""
This problem was asked by Uber.

Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

    Given N = 4, return 1 (4)
    Given N = 17, return 2 (16 + 1)
    Given N = 18, return 2 (9 + 9)
"""
def lowest_power_of_two(number):
	power_of_two = 1
	y = 0
	while 2**(y+1) <= number:
		y += 1
		power_of_two = 2**y
	return power_of_two

def smallest_number(number):
	x = number
	times = 0
	t = ()
	while x != 0:
		power = lowest_power_of_two(x)
		t += (power,)
		x -= power 
		times += 1
	return (times, t)

print(lowest_power_of_two(40))
print(smallest_number(4))
print(smallest_number(17))