def difference(c,sub_list):
	for i in sub_list:
		if abs(c-i) > 1:
			return False
	return True

n = input()
numbers = list(map(int,input().split(' ')))
maxs = []
for i in numbers:
	curr_max = [i]
	for c in numbers:
		if difference(c,curr_max):
			curr_max.append(c)
	maxs.append(len(curr_max))
print(max(maxs)-1)
