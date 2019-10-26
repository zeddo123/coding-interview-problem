"""Queen's Attack II

`https://www.hackerrank.com/challenges/queens-attack-2/problem`
"""
import time

def cells_horizontal(x, y, obstacles_right, obstacles_left, boundary):
    obstacles_right += [(y, boundary+1)]
    obstacles_left += [(y, 0)]

    cells = min((ob2 - x) - 1 for ob1, ob2 in obstacles_right)

    cells += min((x - ob2) - 1 for ob1, ob2 in obstacles_left)

    return cells

def cells_vertical(x, y, obstacles_top, obstacles_down, boundary):
    obstacles_top += [(boundary+1, x)]
    obstacles_down += [(0, x)]

    cells = min((ob1 - y) - 1 for ob1, ob2 in obstacles_top)

    cells += min((y - ob1) - 1 for ob1, ob2 in obstacles_down)

    return cells

def cells_diagonal(x, y, obstacles_top_right, obstacles_down_right, obstacles_top_left, obstacles_down_left, boundary):
    obstacles_top_right += [(y + min(boundary-y,boundary-x), x + min(boundary-y,boundary-x) + 1)]
    obstacles_down_right += [(y - min(y-1,boundary-x), x + min(y-1,boundary-x) + 1 )]
    
    obstacles_top_left += [(y + min(boundary-y,x-1), x - min(boundary-y,x-1) - 1)]
    obstacles_down_left += [(y - min(y-1,x-1), x - min(y-1,x-1) - 1 )]
    
    cells = min((ob2 - x) - 1 for ob1, ob2 in obstacles_top_right)

    cells += min((ob2 - x) - 1 for ob1, ob2 in obstacles_down_right)


    cells += min((x - ob2) - 1 for ob1, ob2 in obstacles_top_left)

    cells += min((x - ob2) - 1 for ob1, ob2 in obstacles_down_left)
    return cells

obstacles_top = []
obstacles_down = []

obstacles_right = []
obstacles_left = []

obstacles_top_left = []
obstacles_top_right = []

obstacles_down_right = []
obstacles_down_left = []

boundary, num_obs = [int(i) for i in input().split(' ')]
y,x = [int(i) for i in input().split(' ')]
obstacles = []

t1 = time.time()
for i in range(num_obs):
    obstacles.append(tuple([int(i) for i in input().split(' ')]))
    
for oby,obx in obstacles:
    if oby > y and obx == x:
        obstacles_top.append((oby,obx))
    if oby < y and obx == x:
        obstacles_down.append((oby,obx))

    if obx > x and oby == y:
        obstacles_right.append((oby,obx))
    if obx < x and oby == y:
        obstacles_left.append((oby,obx))

    if abs(obx - x) == abs(oby - y):
        if oby > y and obx > x:
            obstacles_top_right.append((oby,obx))
        elif oby < y and obx > x:
            obstacles_down_right.append((oby,obx))
        elif oby > y and obx < x:
            obstacles_top_left.append((oby,obx))
        elif oby < y and obx < x:
            obstacles_down_left.append((oby,obx))


cells = cells_horizontal(x, y, obstacles_right, obstacles_left, boundary)

cells += cells_vertical(x, y, obstacles_top, obstacles_down, boundary)

cells += cells_diagonal(x, y, obstacles_top_right, obstacles_down_right, obstacles_top_left, obstacles_down_left, boundary) 
print(cells)
print(time.time() - t1)