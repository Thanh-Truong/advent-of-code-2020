def validNumber(a, listNumbers):
    # two different numbers in list sum up to 'a'
    for b in listNumbers:
        if a/2 != b and (a - b) in listNumbers:
            return True

if __name__ == "__main__":
    preambleSize = 25
    with open('input.txt', 'r') as f:
        numbers = [int(i) for i in f.read().splitlines()]

        for i in range(preambleSize, len(numbers),1):
            if not validNumber(numbers[i], numbers[i-preambleSize:i]):
                print(numbers[i])
                break