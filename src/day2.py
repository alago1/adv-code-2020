def split_line(line):
    words = line.split(" ")
    nums = [int(x) for x in words[0].split("-")]
    return [nums[0], nums[1], words[1][0], words[2]]

def isValid(arg):
    count = 0
    for s in arg[-1]:
        if s == arg[-2]:
            count += 1
    return arg[0] <= count <= arg[1]

def isValid2(arg):
    if arg[-2] == arg[-1][arg[0]-1] and arg[-2] == arg[-1][arg[1]-1]:
        return False
    
    if arg[-2] == arg[-1][arg[0]-1] or arg[-2] == arg[-1][arg[1]-1]:
        return True
    
    return False

file = open("input/day2", 'r')
args = [split_line(x) for x in file.readlines()]

count = 0
for arg in args:
    if isValid2(arg):
        count += 1

print(count)