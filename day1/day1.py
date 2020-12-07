
import datetime
import copy

def main():
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
 
    

if __name__ == "__main__":
    main()