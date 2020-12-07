def binaryJump(sequences, letterToJump):
    pos = 0
    for i in range(len(sequences)):
        if sequences[i] == letterToJump:
            half = 2**(len(sequences) - 1 - i)
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
    # What is the ID of your seat? The missing one
    seatIds.sort()
    for i in range(len(seatIds) - 1):
        if seatIds[i] + 2 == seatIds[i+1]:
            return seatIds[i] + 1

if __name__ == "__main__":
    # Test
    assert toSeatID("FBFBBFFRLR") == 357
    assert toSeatID("BFFFBBFRRR") == 567
    assert toSeatID("FFFBBBFRRR") == 119
    assert toSeatID("BBFFBBFRLL") == 820

    seatIds = toSeatIDs()
    print(partOne(seatIds))
    print(partTwo(list(toSeatIDs())))