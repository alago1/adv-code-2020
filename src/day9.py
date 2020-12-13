file = open('input/day9', 'r')

def hasSum(adds, target):
    known = set()
    for addend in adds:
        if addend in known:
            return True
        known.add(target - addend)
    return False

def partSum(vals, target):
    partialSums = dict()
    s = 0
    for i, val in enumerate(vals):
        s += val

        if s - target in partialSums:
            return (partialSums[s - target], i)

        partialSums[s] = i
    
    return None
    

nums = [int(x) for x in file.read().split('\n')]

addends = nums[:25]
missing = None

for i in range(25, len(nums)):
    if not hasSum(addends, nums[i]):
        missing = nums[i]
        break
    addends[i%25] = nums[i]

if not missing:
    print('uh oh...')
else:
    # print(missing)
    partSumRange = partSum(nums, missing)

    if partSumRange:
        n_range = nums[partSumRange[0]:partSumRange[1]+1]
        print(max(n_range)+min(n_range))
    else:
        print("didn't find a range")