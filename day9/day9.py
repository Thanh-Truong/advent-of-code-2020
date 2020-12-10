
def validNumber(a, ls):
    """a is valid if there are two different numbers in list sum up to a
    """
    for b in ls:
        if a/2 != b and (a - b) in ls:
            return True

def firstInvalidNumber(preambleSize, ls):
    """ Find the first invalid number
    """
    for i in range(preambleSize, len(ls),1):
        if not validNumber(ls[i], ls[i-preambleSize:i]):
            return ls[i]

def twoContiguousNumbers(ls):
    for i in range(len(ls) - 1):
        if ls[i] < ls[i + 1]:
            return True

def findContiguousSetWithSumEquals(value,numbers):
    # Find contiguous set of at least two numbers that sums up to 'firstInvalidNum'
    start = 0
    stop = 0
    for _ in range(len(numbers)):
        #print("{} current {} start {} stop {}".format(numbers[start:stop], numbers[_], start, stop))
        # expand first
        stop +=1
        while sum(numbers[start:stop]) > firstInvalidNumber:
            # throw out elements from the left if sum is bigger
            start = start + 1

        if sum(numbers[start:stop]) == firstInvalidNumber and twoContiguousNumbers(numbers[start:stop]):
            return numbers[start:stop]

if __name__ == "__main__":
    
    with open('input.txt', 'r') as f:
        numbers = [int(i) for i in f.read().splitlines()]
        firstInvalidNumber = firstInvalidNumber(25, numbers)
        print(firstInvalidNumber)
        subSet = findContiguousSetWithSumEquals(firstInvalidNumber, numbers)
        print(min(subSet) + max(subSet))
        