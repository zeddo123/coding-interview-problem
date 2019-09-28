def are_sync(x1, v1, x2, v2):
	if v1 == v2 and x1 == x2:
		return 'YES'
	elif v1 == v2:
		return 'NO'

	if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) > 0:
		return 'YES'
	else:
		return 'NO'

x1, v1, x2, v2 = tuple(map(int,input().split(' ')))
print(are_sync(x1,v1,x2,v2))