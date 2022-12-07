from collections import deque


def restack(file, part1):
    ops = False
    init = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line == "\n":
                ops = True
                stacks = initialize(init)
                continue
            if not ops:
                init += [line[:-2]]
            else:
                moves = int(line[5:7].strip())
                start = int(line[12:14].strip()) - 1
                dest = int(line.strip()[-1]) - 1

                if part1:
                    for _ in range(moves):
                        stacks[dest].append(stacks[start].pop())
                else:
                    list = []
                    for i in range(moves):
                        list.append(stacks[start].pop())

                    stacks[dest].extend(reversed(list))

    solution = ''
    for stack in stacks:
        solution += stack.pop()

    return solution


def initialize(init):
    stacks = []
    nr = int(init[-1][-1])
    for _ in range(nr):
        stacks.append(deque())
    for line in reversed(init[:-1]): #build the stacks from bottom to top
        for i in range(nr):
            if line[1+4*i] != ' ':
                stacks[i].append(line[1+4*i])

    return stacks


def main():
    print("the answer is ")
    print(restack("data/test_data", True))
    print(restack("data/real_data", True))
    print(restack("data/test_data", False))
    print(restack("data/real_data", False))


if __name__ == "__main__":
    main()

