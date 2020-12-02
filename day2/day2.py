
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

    def isValidate(self):
        return self.password

def parseAnInputString(str):
    #"1-3 a: abcde"
    return Password(str)

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            password = Password(line)
            password.toStr()
            if password.isValidate():
                count = count + 1
        print(count)

if __name__ == "__main__":
    main()