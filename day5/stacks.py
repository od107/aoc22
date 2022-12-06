from collections import deque


def part1(file):
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

                for _ in range(moves):
                    stacks[dest].append(stacks[start].pop())

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
    print(part1("data/test_data"))
    print(part1("data/real_data"))
    # print(part2("data/test_data"))
    # print(part2("data/real_data"))


if __name__ == "__main__":
    main()

