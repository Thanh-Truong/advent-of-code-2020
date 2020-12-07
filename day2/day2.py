
class Policy1():    
    def apply(self, password):
        count = sum(map(lambda c : 1 if password.letter in c else 0, password.password))
        return password.min <= count and password.max >= count

class Policy2():
    def apply(self, password):
        return (password.password[password.min - 1] == password.letter) ^ (password.password[password.max - 1] == password.letter)

class Database():
    def __init__(self, lines):
        self.passwords = [Password(line) for line in lines]
        
    def countValidatePasswords(self, policy):
        return sum(map(
            lambda r: 1 if r else 0, map(
                lambda password: policy.apply(password), self.passwords)))
        

class Password():
    def __init__(self, line):
        self.str = line
        self.parse()

    def parse(self):
        str_min = self.str.split("-")[0]
        str_max = self.str[len(str_min)+1:].split(" ")[0]
        str_letter = self.str[len(str_min)+1 + len(str_max)+1:].split(":")[0]
        self.min = int(str_min)
        self.max = int(str_max)
        self.letter = str_letter
        self.password = self.str[len(str_min) +  1 + len(str_max) + 1 + len(str_letter) + 1 + 1:]

    def toStr(self):
        print("min={} max={} letter={} password={}".format(self.min, self.max, self.letter, self.password))

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        database = Database(lines)        
        count = database.countValidatePasswords(Policy1())
        print(count)
        count = database.countValidatePasswords(Policy2())
        print(count)

if __name__ == "__main__":
    main()