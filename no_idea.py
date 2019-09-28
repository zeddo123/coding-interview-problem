happiness = 0
n_m = input()
array = list(map(int,input().split(' ')))
a = set(map(int,input().split(' ')))
b = set(map(int,input().split(' ')))

happiness = sum( (i in a) - (i in b) for i in array )
print(happiness)