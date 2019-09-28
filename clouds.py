n = input()
clouds = input().split(' ')
emma = 0
jumps = 0

while emma != n - 1:
	if emma == n - 2:
		emma += 1
	elif clouds[emma + 2] == '0':
		emma += 2
	else:
		emma += 1
	jumps += 1

print(jumps)