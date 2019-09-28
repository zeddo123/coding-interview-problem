magic_squares = [
			[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
			[[6, 1, 8], [7, 5, 3], [2, 9, 4]],
			[[4, 9, 2], [3, 5, 7], [8, 1, 6]],
			[[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
			[[8, 3, 4], [1, 5, 9], [6, 7, 2]],
			[[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
			[[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
			[[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]
cost = lambda n, o: abs(n - o)

row0 = list(map(int,input().split(' ')))
row1 = list(map(int,input().split(' ')))
row2 = list(map(int,input().split(' ')))

matrix = [row0,row1,row2]
costs = []

for square in magic_squares:
	curr_cost = 0
	for i in range(3):
		for c in range(3):
			curr_cost += cost(square[i][c],matrix[i][c])
	cots.append(curr_cost)

print(min(costs))