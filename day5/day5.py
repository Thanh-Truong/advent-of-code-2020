def binaryJump(sequences, letterToJump):
    pos = 0
    for i in range(len(sequences)):
        half = 2**(len(sequences) - 1 - i)
        if sequences[i] == letterToJump:
            pos = pos + half
    return pos

def toSeatID(boardingPass):
    row = binaryJump(boardingPass[0:7], 'B')
    column = binaryJump(boardingPass[7:10], 'R')
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

if __name__ == "__main__":
    # Test
    assert toSeatID("FBFBBFFRLR") == 357
    assert toSeatID("BFFFBBFRRR") == 567
    assert toSeatID("FFFBBBFRRR") == 119
    assert toSeatID("BBFFBBFRLL") == 820

    seatIds = toSeatIDs()
    print(partOne(seatIds))
    print(partTwo(list(toSeatIDs())))