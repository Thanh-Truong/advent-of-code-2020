import copy

def partOne(instructions):
    visited = [0] * len(instructions)
    value = 0
    current = 0
    while(not visited[current]):
        visited[current] = 1
        # process the instruction
        [op, arg] = instructions[current].split(" ")
        step = 1
        if op == 'acc':
            value = value + int(arg)
        elif op == 'jmp':
            step = int(arg)
        # next
        current = current +  step
    print("Part One = {}".format(value))

def terminateCorrectly(instructions):
    visited = [0] * len(instructions)
    value = 0
    current = 0
    # continue if not the last instruction and there is no infinite loop
    while(current < len(instructions) and not visited[current]):
        visited[current] = 1
        # process the instruction
        [op, arg] = instructions[current].split(" ")
        step = 1
        if op == 'acc':
            value = value + int(arg)
        elif op == 'jmp':
            step = int(arg)
        # next
        current = current +  step
    
    if current == len(instructions):
        return value
    else:
        return 0

def partTwo(instructions):
    value = 0
    swapOps = ["nop", "jmp"]
    for i in range(len(instructions)):
        [op, arg] = instructions[i].split(" ")
        if op in swapOps:
            index = swapOps.index(op)
            newOp = swapOps[1 - index]
            newInstructions = instructions[0:i] + ["{} {}".format(newOp, arg)] + instructions[i+1:]
            value = terminateCorrectly(newInstructions)
            if value != 0:
                break
    print(value)

    


def main():
    with open('input.txt', 'r') as f:
        instructions = f.read().splitlines()
        partOne(instructions)
        partTwo(instructions)

if __name__ == "__main__":
    main()