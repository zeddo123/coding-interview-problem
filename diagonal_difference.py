row = int(input())
left_to_right_diagonal = 0
right_to_left_diagonal = 0

for i in range(row):
	values = list(map(int, input().split(' ')))
	left_to_right_diagonal += values[i]
	right_to_left_diagonal += values[len(values)-i-1]

print(abs(left_to_right_diagonal - right_to_left_diagonal))
