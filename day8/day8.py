def main():
    with open('input.txt', 'r') as f:
            instructions = f.read().splitlines()
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
                current = current +  step if current < len(instructions) - 1 else 0
            print(value)

if __name__ == "__main__":
    main()