file = open('input/day11', 'r')

def occupiedCount(floorMap):
    count = [[0 for x in range(len(floorMap[y]))] for y in range(len(floorMap))]
    directs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for row in range(len(floorMap)):
        for col in range(len(floorMap[row])):
            if floorMap[row][col] in ['L', '#']:
                for i, j in directs:
                    for scale in range(1, max(len(floorMap), len(floorMap[0]))):
                        if 0 <= row + i*scale < len(floorMap) and 0 <= col + j*scale < len(floorMap[i]):
                            view = floorMap[row+i*scale][col+j*scale]
                            if view == '#':
                                count[row][col] += 1
                                break
                            elif view == 'L':
                                break
                        else:
                            break
    
    return count

def evolveMap(floorMap, countMap):
    boardChanged = False
    for row in range(len(floorMap)):
        for col in range(len(floorMap[row])):
            if floorMap[row][col] == 'L' and countMap[row][col] == 0:
                floorMap[row][col] = '#'
                boardChanged = True
            
            elif floorMap[row][col] == '#' and countMap[row][col] >= 5:
                floorMap[row][col] = 'L'
                boardChanged = True

    return boardChanged

map = [list(x) for x in file.read().split('\n')]
countMap = occupiedCount(map)

while evolveMap(map, countMap):
    countMap = occupiedCount(map)

count = 0
for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] == '#':
            count += 1

print(count)