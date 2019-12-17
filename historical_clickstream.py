"""
This problem was asked by Facebook.
We have some historical clickstream data gathered from our site anonymously using cookies.
The histories contain URLs that users have visited in chronological order.

Write a function that takes two users' browsing histories as input 
and returns the longest contiguous sequence of URLs that appear in both.

For example, given the following two users' histories:
user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
user2 = ['/home', '/red', '/login', '/user', '/one', '/pink'] 

You should return the following:
['/login', '/user', '/one']
"""
# the first solution can't find sequences in the middle-right
# O(2n)

user1 = ['home', 'blabla', 'home', 'user', 'cake', 'two', 'one', 'father']
user2 = ['father', 'home', 'user', 'nice', 'user', 'cake', 'two', 'one', 'blabla']

user_min, user_max = (user1, user2) if len(user1) < len(user2) else (user2, user1)

begin = 0
end = len(user_min) - 1
buff = (0, None)
user_max_str = ''.join(user_max)

while end > 0 and begin < len(user_min) - 1:
	if end > begin:
		test_list = user_min[begin:end+1]
		len_test = len(test_list) 
		
		if ''.join(test_list) in user_max_str:
			if len_test > buff[0]:
				buff = (len_test, test_list)
	
	# getting history form the end
	test_list = user_min[0:end+1]
	len_test = len(test_list) 
		
	if ''.join(test_list) in user_max_str:
		if len_test > buff[0]:
			buff = (len_test, test_list)

	# getting history from the beginning
	test_list = user_min[begin:len(user_min)]
	len_test = len(test_list) 
		
	if ''.join(test_list) in user_max_str:
		if len_test > buff[0]:
			buff = (len_test, test_list)

	begin += 1
	end -= 1

print(buff)
# ----------------------------------- Other solution O(n²) <
buff = (0, None)
end = len(user_min)
for p, history in enumerate(user_min):
	for i in reversed(range(p,end)):
		test_list = user_min[p:i+1]
		len_test = len(test_list)
		if ''.join(test_list) in user_max_str and len_test > buff[0]:
			buff = (len_test, test_list)
print(buff)