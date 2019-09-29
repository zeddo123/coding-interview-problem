n = int(input())

scores = sorted(set(map(int,input().split(' '))), reverse = True)

n = int(input())
alice_scores = list(map(int,input().split(' ')))
uniq_alice = set(alice_scores) 
alice_ranks = {}

for s in reversed(scores):
	scores_lower = list(set(filter(lambda a:s > a,uniq_alice)))
	for score in scores_lower:
		alice_ranks[score] = scores.index(s) + 2
		uniq_alice.remove(score)

for i in alice_scores:
	print(alice_ranks.get(i,1))
