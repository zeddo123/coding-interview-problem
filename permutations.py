import time

def permutations(string, begin, end):
	if begin == end:
		return [string]

	permut = []
	for i in range(begin,end):
		fixedstr = string[0:begin] + string[i] + string[begin:i] + string[i+1:]
		# print('fixed ',string[0:begin])
		# print('current ',string[i])
		# print('before ',string[begin:i])
		# print('after ',string[i+1:])
		permut += permutations(fixedstr,begin + 1,end)
	return permut

sr = 'abcdefgglkm'
begining = time.time()
print(permutations(sr,0,len(sr)))
print(time.time() - begining)
