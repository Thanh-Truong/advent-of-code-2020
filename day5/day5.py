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
        print("Begin l = {} and r = {} half = {} letter = {}".format(l, r, half, letter))        
        if letter == 'L':
            r = l + half
        else: # or 'R'
            l = l + half
        print("End l = {} and r = {}".format(l, r))        

    col = r
    return col

def toSeatID(boardingPass):
    row = convertToRow(boardingPass[0:6])
    column = convertToColumn(boardingPass[7:9])
    print("row = {} and col = {}".format(row, column))
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
    #print(partTwo())
