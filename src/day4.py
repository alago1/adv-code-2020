import re

file = open('input/day4', 'r')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = [{y.split(':')[0] : y.split(':')[1] for y in x.replace('\n', ' ').split(' ')} for x in file.read().split('\n\n')]

count = 0
for passport in passports:
    if not all(field in passport for field in fields):
        continue

    if not (len(passport["byr"]) == 4 and 1920 <= int(passport["byr"]) <= 2002):
        continue

    if not (len(passport["iyr"]) == 4 and 2010 <= int(passport["iyr"]) <= 2020):
        continue
        
    if not (len(passport["eyr"]) == 4 and 2020 <= int(passport["eyr"]) <= 2030):
        continue

    if not passport["hgt"].endswith("cm") and not passport["hgt"].endswith("in"):
        continue

    if passport["hgt"].endswith("cm") and not (150 <= int(passport["hgt"][:len(passport["hgt"])-2]) <= 193):
        continue

    if passport["hgt"].endswith("in") and not (59 <= int(passport["hgt"][:len(passport["hgt"])-2]) <= 76):
        continue

    if not passport["hcl"].startswith("#") or not re.match(r"^[0-9, a-f]{6}$", passport["hcl"][1:]):
        continue
    
    if passport["ecl"] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue

    if not re.match(r"^[0-9]{9}$", passport["pid"]):
        continue

    print(passport)
    count += 1


print(count)