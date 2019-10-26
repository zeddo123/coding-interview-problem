"""Queen's Attack II

`https://www.hackerrank.com/challenges/queens-attack-2/problem`
You will be given a square chess board with one queen and a number of obstacles placed on it.
Determine how many squares the queen can attack. 
"""
import time
def cells_horizontal(x, y, obstacles_right, obstacles_left, boundary):
	if obstacles_right != None:
		cells = obstacles_right[1] - x - 1
	else:
		cells =  boundary - x
	
	if obstacles_left != None:
		cells += (x - obstacles_left[1]) - 1
	else:
		cells += x - 1

	return cells

def cells_vertical(x, y, obstacles_top, obstacles_down, boundary):

	if obstacles_top != None:
		cells = obstacles_top[0] - y - 1
	else:
		cells = boundary - y

	if obstacles_down != None:
		cells += y - obstacles_down[0] - 1
	else:
		cells += y - 1

	return cells

def cells_diagonal(x, y, obstacles_top_right, obstacles_down_right, obstacles_top_left, obstacles_down_left, boundary):	
	if obstacles_top_right != None:
		cells = (obstacles_top_right[1] - x) - 1
	else:
		cells = ((x + min(boundary-y,boundary-x) + 1) - x) - 1

	if obstacles_down_right != None:
		cells += (obstacles_down_right[1] - x) - 1
	else:
		cells += ((x + min(y-1,boundary-x) + 1) - x) - 1

	if obstacles_top_left != None:
		cells += (x - obstacles_top_left[1]) - 1
	else:
		cells += (x - (x - min(boundary-y,x-1) - 1)) - 1

	if obstacles_down_left != None:
		cells += (x - obstacles_down_left[1]) - 1
	else:
		cells += (x - (x - min(y-1,x-1) - 1)) - 1

	return cells

obstacles_top = None
obstacles_down = None

obstacles_right = None
obstacles_left = None

obstacles_top_left = None
obstacles_top_right = None

obstacles_down_right = None
obstacles_down_left = None

boundary, num_obs = [int(i) for i in input().split(' ')]
y,x = [int(i) for i in input().split(' ')]
obstacles = []

for i in range(num_obs):
	obstacles.append(tuple([int(i) for i in input().split(' ')]))
	
t1 = time.time()
for oby,obx in obstacles:
	if obx == x:
		if oby > y:
			obstacles_top = (oby,obx) if not obstacles_top else (oby,obx) if oby < obstacles_top[0] else obstacles_top
		if oby < y:
			obstacles_down = (oby,obx) if not obstacles_down else (oby,obx) if oby > obstacles_down[0] else obstacles_down

	if oby == y:
		if obx > x:
			obstacles_right = (oby,obx) if not obstacles_right else (oby,obx) if obx < obstacles_right[1] else obstacles_right
		if obx < x:
			obstacles_left = (oby,obx) if not obstacles_left else (oby,obx) if obx > obstacles_left[1] else obstacles_left

	if abs(obx - x) == abs(oby - y):
		if oby > y and obx > x:
			obstacles_top_right = (oby,obx) if not obstacles_top_right else (oby,obx) if (obx - x) < (obstacles_top_right[1] - x) else obstacles_top_right
		elif oby < y and obx > x:
			obstacles_down_right = (oby,obx) if not obstacles_down_right else (oby,obx) if (obx - x) < (obstacles_down_right[1] - x) else obstacles_down_right
		elif oby > y and obx < x:
			obstacles_top_left = (oby,obx) if not obstacles_top_left else (oby,obx) if (x - obx) < (x - obstacles_top_left[1]) else obstacles_top_left
		elif oby < y and obx < x:
			obstacles_down_left = (oby,obx) if not obstacles_down_left else (oby,obx) if (x - obx) < (x - obstacles_down_left[1]) else obstacles_down_left

cells = cells_horizontal(x, y, obstacles_right, obstacles_left, boundary)

cells += cells_vertical(x, y, obstacles_top, obstacles_down, boundary)

cells += cells_diagonal(x, y, obstacles_top_right, obstacles_down_right, obstacles_top_left, obstacles_down_left, boundary) 

print(cells)
print(time.time() - t1)