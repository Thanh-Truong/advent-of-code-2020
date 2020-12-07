
def policy1(password):
    count = sum(map(lambda c : 1 if password.letter in c else 0, password.password))
    return password.min <= count and password.max >= count

def policy2(password):
    return (password.password[password.min - 1] == password.letter) ^ (password.password[password.max - 1] == password.letter)

class Password():
    def __init__(self, line):
        str_min = line.split("-")[0]
        str_max = line[len(str_min)+1:].split(" ")[0]
        str_letter = line[len(str_min)+1 + len(str_max)+1:].split(":")[0]
        self.min = int(str_min)
        self.max = int(str_max)
        self.letter = str_letter
        self.password = line[len(str_min) +  1 + len(str_max) + 1 + len(str_letter) + 1 + 1:]

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        passwords = [Password(line) for line in lines]
        count = len(list(filter(lambda password: policy1(password), passwords)))
        print("Part One: {}".format(count))
        count = len(list(filter(lambda password: policy2(password), passwords)))
        print("Part Two: {}".format(count))

if __name__ == "__main__":
    main()