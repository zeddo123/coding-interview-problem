"""
	Find all the sums that give K
"""
k = 17

import time
print('--experiment 1-- O(n²)')
l = [1,3,4,7,0,10,17,13,15,2]
print(l)
d = time.time()
for i in l :
	for j in l:
		if i + j == k :
			print(i, ' + ' ,j)
f = time.time()
print(f-d)

print('--experiment 2-- O(n)')
l = [1,3,4,7,0,10,17,13,15,2]
l.sort()
print(l)
d = time.time()
for i in l :
	p = len(l)-1
	while i + l[p] >= k and p >=l.index(i):
		if i + l[p] == k :
			print(i, ' + ' ,l[p])
			break
		elif i + l[p] > k:
			p -= 1 
f = time.time()
print(f-d)
