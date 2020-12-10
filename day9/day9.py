def validNumber(a, listNumbers):
    # two different numbers in list sum up to 'a'
    for b in listNumbers:
        if a/2 != b and (a - b) in listNumbers:
            return True

def firstInvalidNumber(preambleSize):
    for i in range(preambleSize, len(numbers),1):
        if not validNumber(numbers[i], numbers[i-preambleSize:i]):
            return numbers[i]

def twoContiguousNumbers(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            return True

def findContiguousSetWithSumEquals(value,numbers):
    # Find contiguous set of at least two numbers that sums up to 'firstInvalidNum'
    start = 0
    stop = 0
    for i in range(len(numbers)):
        #print("{} current {} start {} stop {}".format(numbers[start:stop], numbers[i], start, stop))
        total = sum(numbers[start:stop])

        # expand
        if total + numbers[i] < firstInvalidNumber:
            stop += 1
        elif total + numbers[i] >= firstInvalidNumber:
            stop += 1
            while sum(numbers[start:stop]) > firstInvalidNumber:
                # throw out elements from the left
                start = start + 1

        # newTotal == firstInvalidNumber
        if sum(numbers[start:stop]) == firstInvalidNumber and twoContiguousNumbers(numbers[start:stop]):
            return numbers[start:stop]

if __name__ == "__main__":
    
    with open('input.txt', 'r') as f:
        numbers = [int(i) for i in f.read().splitlines()]
        firstInvalidNumber = firstInvalidNumber(preambleSize=25)
        print(firstInvalidNumber)
        subSet = findContiguousSetWithSumEquals(firstInvalidNumber, numbers)
        print(min(subSet) + max(subSet))
        