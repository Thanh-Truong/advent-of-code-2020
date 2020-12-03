def foo():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        array = []
        for line in lines:
            print("{} {} ".format(line, len(line)))
            array.append(line)

def makeArray():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()       
        array = []
        for line in lines:
            array.append(line)
    return array

def countTreesWithSlope(array, right, down):
    countTrees = 0
    col = 0
    for row in range(len(array)):
        col = row * right
        checkPoint = col % len(array[row])
        if row != 0: # start position
            if array[row][checkPoint] == '#':
                countTrees = countTrees + 1
        #print("row = {} col = {} checkPoint = {} value = {} trees = {}".format(row, col, checkPoint, array[row][checkPoint], countTrees))
    return countTrees

def main():
    array = makeArray()
    print(countTreesWithSlope(array, right=3, down=1))

if __name__ == "__main__":
    main()