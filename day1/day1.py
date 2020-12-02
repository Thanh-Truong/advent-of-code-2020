
import datetime
import copy

CURRENT_YEAR = datetime.date.today().year
YEAR = [-1] * (CURRENT_YEAR + 1)
    
def exists(i, array):
    return array[i] == i

def findPairsOfNumbers(array, sum):
    # Go through the YEAR array and sum up
    length = len(array)
    for i in range(0, length):
        if exists(i, array):
            j = sum - i
            if exists(j, array):
                yield(i, j)
                array[j] = - 1
        #array[i] = -1
        

def findTripleOfNumbers(array, sum):
    # Go through the YEAR array and sum up
    for i in range(0, len(array)):
        if exists(i, array):
            sub_sum = sum - i
            for j, k in findPairsOfNumbers(array[0: sub_sum], sub_sum):
                #print("found {} {} {} {}".format(i, j, k, sub_sum))
                yield(i, j, k)

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
    for i, j in findPairsOfNumbers(array[0: CURRENT_YEAR], CURRENT_YEAR):
        print(i*j)
    
    array = copy.copy(YEAR)
    for i, j, k in findTripleOfNumbers(array, CURRENT_YEAR):
       print(i*j*k)

if __name__ == "__main__":
    main()