'''
For example, consider just the first seven characters of FBFBBFF RLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
'''
def convertToRow(sequences):
    l = 0
    r = 127
    for i in range(len(sequences)):
        #print("l={} r={} letter = {}".format(l, r, sequences[i]))
        half = 2**(7 - i - 1)
        if sequences[i] == 'F':
            r = r - half
        else: # or 'B'
            l = l + half
    return l

'''Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.'''
def convertToColumn(sequences):
    l = 0
    r = 7
    for i in range(len(sequences)):
        half = 2**(3 - i - 1)
        if sequences[i] == 'L':
            r = r - half
        else: # or 'B'
            l = l + half
    return r

def toSeatID(boardingPass):
    row = convertToRow(boardingPass[0:6])
    column = convertToColumn(boardingPass[7:10])
    #print("row = {} and col = {} ".format(row, column))
    return row * 8 + column

def toSeatIDs():
    with open('input.txt', 'r') as f:
        boardingPasses = f.read().splitlines()
        return map(toSeatID, boardingPasses)

def partOne(seatIds):
    # What is the highest seat ID on a boarding pass?
    return max(seatIds)

def partTwo(seatIds):
    # What is the ID of your seat?
    seatIds = list(seatIds)
    seatIds.sort()
    lastId = -1
    for i in seatIds:
        if (lastId != -1 and i - lastId ==2):
            return i - 1
        lastId = i
        

if __name__ == "__main__":
    # Test
    assert toSeatID("FBFBBFFRLR") == 357
    assert toSeatID("BFFFBBFRRR") == 567
    assert toSeatID("FFFBBBFRRR") == 119
    assert toSeatID("BBFFBBFRLL") == 820

    seatIds = toSeatIDs()
    print(partOne(seatIds))
    print(partTwo(toSeatIDs()))
    
    

    