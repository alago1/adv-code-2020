import copy

file = open('input/day8', 'r')

def isFinite(insts):
    i = 0
    acc = 0
    ran_insts = set()

    while i < len(insts):
        if i in ran_insts:
            # print('reran ' + str(i+1))
            return False
        else:
            ran_insts.add(i)

        if insts[i][0] == 'acc':
            acc += insts[i][1]
            i += 1
        elif insts[i][0] == 'jmp':
            i += insts[i][1]
        else:
            i += 1
    
    print(acc)
    return True


instructions = [[x.split(' ')[0], int(x.split(' ')[1])] for x in file.read().split('\n')]

for i in range(len(instructions)):
    if instructions[i][0] in ['jmp', 'nop']:
        t = instructions[i].copy()
        t[0] = 'jmp' if t[0] == 'nop' else 'nop'
        print('trying ' + str(i+1) + ' from ' + instructions[i][0] + " " + str(instructions[i][1]) + ' to ' + t[0] + " " + str(t[1]))
        
        instructions[i] = t
        
        if isFinite(instructions):
            print('success ' + str(i+1))
            break
        else:
            print('failed ' + str(i+1))
        instructions[i][0] = 'jmp' if t[0] == 'nop' else 'nop'
