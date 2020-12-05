def convertToRow(sevenLetters):
    l = 0
    r = 127
    for letter in sevenLetters:
        half = round((r - l)/2)
        if letter == 'F':
            r = l + half
        else: # or 'B'
            l = l + half
    row = l
    return row

def convertToColumn(threeLetters):
    l = 0
    r = 7
    for letter in threeLetters:
        half = round((r - l)/2)
        if letter == 'L':
            r = l + half
        else: # or 'R'
            l = l + half
    col = l
    return col

def toSeatID(boardingPass):
    row = convertToRow(boardingPass[0:6])
    column = convertToColumn(boardingPass[7:9])
    return row * 8 + column

def partOne():
    # What is the highest seat ID on a boarding pass?
    with open('input.txt', 'r') as f:
        boardingPasses = f.read().splitlines()
        return max(map(toSeatID, boardingPasses))

if __name__ == "__main__":
    #print(convertToRow("FBFBBFF"))
    #print(convertToColumn("RLR"))
    print(partOne())
