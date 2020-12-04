import re

def isValidPartTwo(passport):
    '''
    
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

    '''
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl']
    # 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    validateFunctions = [isByrValid, isIyrValid, isEyrValid, isHgtValid, isHclValid]
    # ,  isHgtValid, isHclValid, isEclValid, isPidValid]
    for i in range(len(required)):
        if not validateFunctions[i](passport.get(required[i])):
            return False
    return True

def isByrValid(byr):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    try:
        return int(byr) >= 1920 and int(byr) <= 2002
    except Exception:
        return False

def isIyrValid(iyr):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    try:
        return int(iyr) >= 2010 and int(iyr) <= 2020
    except Exception:
        return False

def isEyrValid(eyr):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    try:
        return int(eyr) >= 2020 and int(eyr) <= 2030
    except Exception:
        return False

def isHgtValid(hgt):
    # hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76.
    try:
        unit = hgt[len(hgt) -2 : len(hgt)]
        num = int(hgt[:len(hgt) - 2])
        if unit == "cm":
            return int(num) >= 150 and int(num) <= 193
        elif unit == "in":
            return int(num) >= 59 and int(num) <= 76
        else:
            return False
    except Exception:
        return False

def isHclValid(hcl):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    return re.search("^#[0-9a-f]{6}$", hcl)

def isEclValid(ecl):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def isPidValid(pid):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    re.search("^[0-9]{9}$", pid)

def allRequiredFieldsPresent(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    #optional = ['cid']
    return len(list(filter(lambda k: passport.get(k), required))) == len(required)

def makePassportFromStr(str):
    passport = {}
    keyValues = str.split(" ")
    for kv in keyValues:
        [k,v] = kv.split(":")
        passport[k] = v
    return passport

def listInformationFromFile():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        informationLines = []
        for line in lines:
            if line == "":
                yield " ".join(informationLines)
                informationLines = []
            else:
                informationLines.append(line)
        yield " ".join(informationLines)

if __name__ == "__main__":
    passports = map(lambda info: makePassportFromStr(info), listInformationFromFile())
    numValidPassports = len(list(filter(lambda p: allRequiredFieldsPresent(p), passports)))
    print(numValidPassports)

    passports = map(lambda info: makePassportFromStr(info), listInformationFromFile())
    numValidPassports = len(list(filter(lambda p: isValidPartTwo(p), passports)))
    print(numValidPassports)

    #print(isHgtValid("177cm"))