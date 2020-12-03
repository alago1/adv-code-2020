file = open('input/day3', 'r')

lines = file.readlines()

def countSlope(lines, x, y):
    count = 0
    index = 0
    for i in range(len(lines)):
        if i % y != 0:
            continue
        if lines[i][index] == '#':
            count += 1
        index += x
        index %= len(lines[0])-1
    
    return count

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

prod = 1
for slope in slopes:
    prod *= countSlope(lines, *slope)

print(prod)