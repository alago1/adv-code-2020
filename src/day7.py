file = open('input/test', 'r')

# single \n between groups
rules = {' '.join(x.split(" contain ")[0].split(' ')[:-1]):[' '.join(y.split(' ')[:-1]) for y in x.split(" contain ")[1].split(', ')] for x in file.read().split('\n')}
names = [bagName for bagName in rules]
target = "shiny gold"
# stepsToTarget = {bagName: 0 if bagName != target else 1 for bagName in rules}

# print(rules)

def rec(bag):
    # print(bag)
    if rules[bag][0] == "no other":
        return 0
    
    count = 0
    for dep in rules[bag]:
        space_split = dep.split(" ")
        n = int(space_split[0])
        name = ' '.join(space_split[1:])
        count += n * (1 + rec(name))
    
    # print(bag, count)
    return count

print(rec(target))

# for i in range(len(stepsToTarget)):
#     for bagName in names:
#         count = 0
#         if bagName == target:
#             continue

#         for dep in rules[bagName]:
#             if dep == 'no other':
#                 break
#             space_split = dep.split(" ")
#             n = int(space_split[0])
#             name = ' '.join(space_split[1:])
#             count += n * stepsToTarget[name]
#         stepsToTarget[bagName] = count # 1 if count > 0 else 0

# countPaths = 0
# for bagName in names:
#     countPaths += stepsToTarget[bagName]
