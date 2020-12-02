
class Password():
    def __init__(self, line):
        self.min = None
        self.max = None
        self.letter = None
        self.password = line
        self.str = line
    
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
            if password.isValidate():
                count = count + 1
        print(count)

if __name__ == "__main__":
    main()