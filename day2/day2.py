
class Policy1():
    def __init__(self):
        pass
    
    def apply(self, password):
        count = 0
        for c in password.password:
            if c == password.letter:
                count = count + 1
        return password.min <= count and password.max >= count

class Policy2():
    def __init__(self):
        pass
    
    def apply(self, password):
        position1 = password.min - 1
        position2 = password.max - 1
        if position1 < len(password.password) and position2 < len(password.password):
            return (password.password[position1] == password.letter) ^ (password.password[position2] == password.letter)
        else:
            raise ValueError("Something wrong")
        

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
        count = database.countValidatePasswords(Policy2())
        print(count)
    
def quicker():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        countPolicy1 = 0
        countPolicy2 = 0
        for line in lines:
            # 8-10 h: mbhzhhhhhkhhhhhhh
            min = line.split("-")[0]
            tokens = line[len(min)+1:].split(" ")
            max = tokens[0]
            letter = tokens[1][0]
            password = tokens[2]
            #print("{} {} {} {}".format(min, max, letter, password))
            # Policy 1
            countLetter = 0
            for c in password:
                if c == letter:
                    countLetter = countLetter + 1
            if countLetter >= int(min) and countLetter <= int(max):
                countPolicy1 = countPolicy1 + 1

            # Policy 2
            if (password[int(min) - 1] == letter) ^ (password[int(max) - 1] == letter):
                countPolicy2 = countPolicy2 + 1
        print(countPolicy1)
        print(countPolicy2)


if __name__ == "__main__":
    main()
    quicker()