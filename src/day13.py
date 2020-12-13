file = open('input/day13', 'r')

lines = file.read().split('\n')

buses = [((10*int(x[1]) - x[0])%(int(x[1])), int(x[1])) for x in enumerate(lines[1].split(',')) if x[1] != 'x']

# solve the linear congruence system from here
# https://comnuan.com/cmnn02/cmnn0200a/cmnn0200a.php
print(buses)