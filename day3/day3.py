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
    row = 0
    while row < len(array):
        col = row * right
        checkPoint = col % len(array[row])
        if row != 0:  # start position
            if array[row][checkPoint] == '#':
                countTrees = countTrees + 1
        #print("row = {} col = {} checkPoint = {} value = {} trees = {}".format(row, col, checkPoint, array[row][checkPoint], countTrees))
        row = row + down
    return countTrees


def main():
    array = makeArray()
    # Part 1
    print(countTreesWithSlope(array, right=3, down=1))
    # Part 2
    result = countTreesWithSlope(array, right=1, down=1) * countTreesWithSlope(array, right=3, down=1) * countTreesWithSlope(
        array, right=5, down=1) * countTreesWithSlope(array, right=7, down=1) * countTreesWithSlope(array, right=1, down=2)
    print(result)


if __name__ == "__main__":
    main()
