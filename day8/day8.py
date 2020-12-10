def execute(instructions):
    visited = [0] * len(instructions)
    value = 0
    current = 0
    while(current < len(instructions) and not visited[current]):
        visited[current] = 1
        # process the instruction
        [op, arg] = instructions[current].split(" ")
        step = 1
        if op == 'acc':
            value += int(arg)
        elif op == 'jmp':
            step = int(arg)
        # next
        current += step
    return value, current

def partTwo(instructions):
    value = 0
    swapOps = ["nop", "jmp"]
    for i in range(len(instructions)):
        [op, arg] = instructions[i].split(" ")
        if op in swapOps:
            index = swapOps.index(op)
            newOp = swapOps[1 - index]
            newInstructions = instructions[0:i] + ["{} {}".format(newOp, arg)] + instructions[i+1:]
            value, current = execute(newInstructions)
            if current == len(instructions):
                break
    print("Part Two : {}".format(value))

def main():
    with open('input.txt', 'r') as f:
        instructions = f.read().splitlines()
        value, _ = execute(instructions)
        print("Part One : {}".format(value))
        partTwo(instructions)

if __name__ == "__main__":
    main()