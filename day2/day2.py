
class Policy1():
    def __init__(self):
        pass
    
    def apply(self, password):
        count = 0
        for c in password.password:
            if c == password.letter:
                count = count + 1
        return password.min <= count and password.max >= count

class Database():
    def __init__(self, lines):
        self.passwords = []
        for line in lines:
            self.passwords.append(Password(line))

    def countValidatePasswords(self, policy):
        count = 0
        for password in self.passwords:
            if policy.apply(password):
                count = count + 1
        return count

class Password():
    def __init__(self, line):
        self.min = None
        self.max = None
        self.letter = None
        self.password = None
        self.str = line
        self.parse()

    def parse_min(self, str):
        tokens = str.split("-")
        return tokens[0]
    
    def parse_max(self, str):
        tokens = str.split(" ")
        return tokens[0]
    
    def parse_letter(self, str):
        tokens = str.split(":")
        return tokens[0]

    def parse(self):
        str_min = self.parse_min(self.str)
        str_max = self.parse_max(self.str[len(str_min)+1:])
        str_letter = self.parse_letter(self.str[len(str_min)+1 + len(str_max)+1:])
        self.min = int(str_min)
        self.max = int(str_max)
        self.letter = str_letter
        self.password = self.str[len(str_min) +  1 + len(str_max) + 1 + len(str_letter) + 1 + 1:]

    def toStr(self):
        print("min={} max={} letter={} password={}".format(self.min, self.max, self.letter, self.password))

    def isValidate_1(self):
        count = 0
        for c in self.password:
            if c == self.letter:
                count = count + 1
        return self.min <= count and self.max >= count

def parseAnInputString(str):
    #"1-3 a: abcde"
    return Password(str)

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        database = Database(lines)        
        count = database.countValidatePasswords(Policy1())
        print(count)

if __name__ == "__main__":
    main()