
import datetime
import copy

CURRENT_YEAR = datetime.date.today().year
YEAR = [-1] * (CURRENT_YEAR + 1)

def exists(i, array):
    return array[i] == i

def findPairsOfNumbers(array):
    length = len(array)
    sum = length - 1
    # Go through the YEAR array and sum up
    for i in range(0, sum):
        if exists(i, array):
            j = sum - i
            if exists(j, array):
                yield(i, j)
                # mark j as done
                array[j] = -1

def main():
    # Fill in the YEAR array with input values
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            i = int(line)
            if i > CURRENT_YEAR:
                raise ValueError("Input value is greater than {}".format(CURRENT_YEAR))
            YEAR[i] = i

    array = copy.copy(YEAR)
    # Go through the YEAR array and sum up
    for i, j in findPairsOfNumbers(array):
        print(i*j)

if __name__ == "__main__":
    main()