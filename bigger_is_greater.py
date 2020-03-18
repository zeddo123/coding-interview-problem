#Lexicographical order is often known as alphabetical order when dealing with strings.
#A string is greater than another string if it comes later in a lexicographically sorted list.
#Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
#	It must be greater than the original word
#	It must be the smallest word that meets the first condition

def algo(s):
    s = list(s)
    for i in reversed(range(len(s))):
        after = sorted(s[i+1:])
        target = sorted((c for c in after if s[i] < c))
        if target != []:
            s[i] , target[0] = target[0], s[i]
            after.remove(s[i])
            after.append(target[0])
            s[i+1:] = sorted(after)
            print(''.join(s))
            return
    print('no answer')

n = int(input())
words = []
for i in range(n):
    words.append(input())

for word in words:
    algo(word)