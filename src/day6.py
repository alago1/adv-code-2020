file = open('input/day6', 'r')

group_answers = [x.split('\n') for x in file.read().split('\n\n')]

def groupYesCount(group):
    s = {x:0 for x in 'abcdefghijklmnopqrstuvwxyz'}
    for answer in group:
        for letter in answer:
            s[letter] += 1
    
    c = 0
    for k in s:
        if s[k] == len(group):
            c += 1
    return c

count = 0
for group in group_answers:
    count += groupYesCount(group)


print(count)