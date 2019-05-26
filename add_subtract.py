"""
Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:

add_subtract(7) -> 7

add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0

add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
"""

def add_subtract(numbers):
	signe = 1
	sum_add_subtract = numbers[0]
	for number in numbers[1:]:
		sum_add_subtract += signe * number
		signe *= -1
	return sum_add_subtract

print(add_subtract([7]))
print(add_subtract([1, 2, 3]))
print(add_subtract([-5, 10, 3, 9]))