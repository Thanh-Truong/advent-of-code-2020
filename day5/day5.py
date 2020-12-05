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
    row = 0
    for i in range(len(sequences)):
        half = 2**(6 - i)
        if sequences[i] == 'B':
            row = row + half
    return row

'''Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.'''
def convertToColumn(sequences):
    col = 0
    for i in range(len(sequences)):
        half = 2**(2 - i)
        if sequences[i] == 'R':
            col = col + half
    return col

def toSeatID(boardingPass):
    row = convertToRow(boardingPass[0:7])
    column = convertToColumn(boardingPass[7:10])
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
    seatIds.sort()
    lastId = -1
    for i in seatIds:
        if (lastId != -1) and (i - lastId == 2):
            return(i - 1)
        lastId = i

def quicker():
    with open('input.txt', 'r') as f:
        boardingPasses = f.read().splitlines()
        
        maxId = - 1
        ids= []
        for bp in boardingPasses:
            row = 0
            col = 0
            for i in range(7):                
                if bp[i] == 'B':
                    row = row + 2**(6 - i)
            
            for i in range(7, 10):                
                if bp[i] == 'R':
                    col = col + 2**(9 - i)
            id = row*8 + col
            ids.append(id)
            if maxId < id:
                maxId = id
        print(maxId)
        lastId = -1
        ids.sort()
    
        for i in ids:
            if (lastId != -1) and i - lastId == 2:
                print(i - 1)
            lastId = i

if __name__ == "__main__":
    # Test
    assert toSeatID("FBFBBFFRLR") == 357
    assert toSeatID("BFFFBBFRRR") == 567
    assert toSeatID("FFFBBBFRRR") == 119
    assert toSeatID("BBFFBBFRLL") == 820

    seatIds = toSeatIDs()
    print(partOne(seatIds))
    print(partTwo(list(toSeatIDs())))
    quicker()
    
    

    