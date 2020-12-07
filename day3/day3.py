def makeArray():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()

def countTreesWithSlope(array, right, step):
    count = 0
    row = 0
    while row < len(array):
        if row != 0:  # start position
            checkPoint = row * right % len(array[row])
            if array[row][checkPoint] == '#':
                count = count + 1
        row = row + step
    return count


def main():
    array = makeArray()
    # Part 1
    print(countTreesWithSlope(array, right=3, step=1))
    # Part 2
    result = countTreesWithSlope(array, right=1, step=1) * countTreesWithSlope(array, right=3, step=1) * countTreesWithSlope(
        array, right=5, step=1) * countTreesWithSlope(array, right=7, step=1) * countTreesWithSlope(array, right=1, step=2)
    print(result)


if __name__ == "__main__":
    main()
