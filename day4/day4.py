import re
from functools import reduce

def isValidPartTwo(passport):
    rules = {
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        'byr': lambda byr: 1920 <= int(byr) <= 2002,
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
        'hgt': isHgtValid,
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        'hcl': lambda hcl: hcl and re.search("^#[0-9a-f]{6}$", hcl),
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        'ecl': lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        'pid': lambda pid: pid and re.search("^[0-9]{9}$", pid)}
    try:
        # apply rules
        res = map((lambda field: rules[field](passport.get(field))), rules)
        return reduce(lambda x, y: x and y, res)
    except Exception:
        return False

def isHgtValid(hgt):
    # hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76.
    unit = hgt[len(hgt) -2 : len(hgt)]
    num = int(hgt[:len(hgt) - 2])
    return (unit == "cm" and 150 <= int(num) <= 193) or (
        unit == "in" and 59 <= int(num) <= 76)

def allRequiredFieldsPresent(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    # all fields are present.
    return len(list(filter(lambda field: passport.get(field), fields))) == len(fields)

def makePassportFromStr(str):
    passport = {}
    keyValues = str.split(" ")
    for kv in keyValues:
        [k,v] = kv.split(":")
        passport[k] = v
    return passport

def listGroups():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        group = []
        for line in lines:
            if line == "":
                yield " ".join(group)
                group.clear()
            else:
                group.append(line)
        yield " ".join(group) # last group

if __name__ == "__main__":
    passports = map(lambda info: makePassportFromStr(info), listGroups())
    numValidPassports = len(list(filter(lambda p: allRequiredFieldsPresent(p), passports)))
    print(numValidPassports)

    passports = map(lambda info: makePassportFromStr(info), listGroups())
    numValidPassports = len(list(filter(lambda p: isValidPartTwo(p), passports)))
    print(numValidPassports)
