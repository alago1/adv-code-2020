file = open('input/day10', 'r')

def isValid(d):
    return ( 1 <= d <= 3 )

adapters = [int(x) for x in file.read().split('\n')]

adapters.sort()
adapters.insert(0, 0) # add outlet
adapters.append(adapters[-1] + 3) # add phone adapter

count = [1, 1, 2] # possible combinations up to index

for i in range(3, len(adapters)):
    d = adapters[i] - adapters[i-1]
    c = 0

    if not ( 1 <= d <= 3 ):
        count.append(0)
        break
    else:
        c += count[i-1]
    
    if isValid(adapters[i] - adapters[i-2]):
        c += count[i-2]
    
    if isValid(adapters[i] - adapters[i-3]):
        c += count[i-3]
    
    count.append(c)

# print(adapters)
# print(count)
print(count[-1])