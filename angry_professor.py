# Get number of test cases
n = int(input())
answers = []
append = answers.append

for i in range(n):
	students, threshold = list(map(int,input().split()))
	times = list(map(int,input().split()))
	if len(times) - sum(1 for t in times if t > 0) >= threshold:
		append('NO')
	else:
		append('YES')

for i in answers:
	print(i)