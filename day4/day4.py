def isValid(passport):
    ''' 
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    '''
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    #optional = ['cid']
    # All required field exist
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

if __name__ == "__main__":
    passports = map(lambda info: makePassportFromStr(info), listInformationFromFile())
    numValidPassports = len(list(filter(lambda p: isValid(p), passports)))
    print(numValidPassports)