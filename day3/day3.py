def foo():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        array = []
        for line in lines:
            print("{} {} ".format(line, len(line)))
            array.append(line)

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()       
        array = []
        for line in lines:
            array.append(line)
        countTrees = 0
        col = 0
        for row in range(len(array)):
            col = row * 3
            #print(len(array[row]))
            checkPoint = col % len(array[row])
            if row != 0:
                if array[row][checkPoint] == '#':
                    countTrees = countTrees + 1
            #print("row = {} col = {} checkPoint = {} value = {} trees = {}".format(row, col, checkPoint, array[row][checkPoint], countTrees))
    print(countTrees)

if __name__ == "__main__":
    main()