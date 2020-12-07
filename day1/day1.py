
import datetime
import copy
''' 
567171
----------------
212428694

'''

def quicker():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        numbers = list(map(lambda line: int(line), lines))
        for i in numbers:
            if (2020 - i) in numbers:
                print("Part One : {}".format((2020-i)*i))
                break
        
        size = len(numbers)
        for i in range(size - 2):
            for j in range(i, size - 1):
                for k in range(j, size):
                    if numbers[i] + numbers[j] + numbers[k]== 2020:
                        print("Part Two : {}".format(numbers[i]*numbers[j]*numbers[k]))
                        break
        

    """ size = len(listNumbers)
    # Part 1
    for i in range(size):
        for j in range(size - i - 1):
            if listNumbers[i] + listNumbers[j]== 2020:
                print(listNumbers[i]*listNumbers[j])
    print("----------------")
    # Part 2
    for i in range(size):
        for j in range(size - i - 1):
            for k in range(size - i - j - 1):
                if listNumbers[i] + listNumbers[j] + listNumbers[k]== 2020:
                    print(listNumbers[i]*listNumbers[j]*listNumbers[k])
        
 """
    

if __name__ == "__main__":
    quicker()