file = open('input/day12', 'r')

instructs = [[x[0], int(x[1:]) if x[0] not in 'LR' else int(x[1:])//90] for x in file.read().split('\n')]

waypoint = [10, 1]
ship = [0, 0]

for inst in instructs:
    if inst[0] == 'N':
        waypoint[1] += inst[1]
    if inst[0] == 'S':
        waypoint[1] -= inst[1]
    if inst[0] == 'E':
        waypoint[0] += inst[1]
    if inst[0] == 'W':
        waypoint[0] -= inst[1]
    if inst[0] == 'F':
        ship[0] += inst[1]*waypoint[0]
        ship[1] += inst[1]*waypoint[1]
    if inst[0] in 'LR':
        t = [waypoint[0], waypoint[1]]
        for i in range(inst[1]):
            if inst[0] == 'R':
                t = [t[1], -t[0]] # 90 degree clockwise rotation
            else:
                t = [-t[1], t[0]]
        waypoint[0] = t[0]
        waypoint[1] = t[1]
    
    # print(inst, ship, waypoint)

print(abs(ship[0]) + abs(ship[1]))
