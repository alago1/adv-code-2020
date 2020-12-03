import functools

file = open('input/day1', 'r')
nums = [int(x) for x in file.readlines()]

def sum2_solver(vals, target):
    seen = set()

    for n in vals:
        if n in seen:
            return [n, target-n]
        seen.add(target - n)
    
    return False

def sum3_solver(vals, target):
    for n in vals:
        t = sum2_solver(vals, target - n)
        if t:
            return [n] + t
    
    return False

output = sum3_solver(nums, 2020)
print(output)
print("Product: ", functools.reduce(lambda a, b: a*b, output))

# 447 + 611 + 962