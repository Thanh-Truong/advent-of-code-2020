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
    for i in range(1, len(sequences)):
        half = 2**(7 - i)
        if sequences[i - 1] == 'F':
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
    for i in range(1, len(sequences)):
        half = 2**(3 - i)
        if sequences[i - 1] == 'L':
            r = r - half
        else: # or 'B'
            l = l + half
    return r

def toSeatID(boardingPass):
    row = convertToRow(boardingPass[0:6])
    column = convertToColumn(boardingPass[7:10])
    #print("row = {} and col = {} and id = {}".format(row, column, row * 8 + column))
    return row * 8 + column

def partOne():
    # What is the highest seat ID on a boarding pass?
    with open('input.txt', 'r') as f:
        boardingPasses = f.read().splitlines()
        return max(map(toSeatID, boardingPasses))

def partTwo():
    # What is the ID of your seat?
    with open('input.txt', 'r') as f:
        boardingPasses = f.read().splitlines()
        seatIds = list(map(toSeatID, boardingPasses))
        seatIds.sort()
        seats = {}
        for id in seatIds:
            seats[id] = 'None'
        a = list(seats.keys())
        for i in a:
            if not (i + 1 in a) and (i +2) in a:
                print(i + 1)
        #seatIds.sort()
        #return seatIds
        

if __name__ == "__main__":
    print(partOne())
    print(partTwo())
    #print(toSeatID("FBFBBFFRLR"))

    #print(toSeatID("BFFFBBFRRR"))
    #print(toSeatID("FFFBBBFRRR"))
    #print(convertToRow("FBFBBFFRLR"[0:6]))
    #print(convertToColumn("FBFBBFFRLR"[7:10]))