def count(file):
    priority = {}

    for i in range(26):
        priority[chr(ord('a')+i)] = i + 1
        priority[chr(ord('A')+i)] = 27 + i

    total_part1 = part1(file, priority)
    total_part2 = part2(file, priority)

    return total_part1, total_part2


def part1(file, priority):
    total = 0
    with open(file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            first = line[:len(line) // 2]
            second = line[len(line) // 2:]

            for letter in first:
                if letter in second:
                    total += priority[letter]
                    break
    return total


def part2(file, priority):
    total = 0
    with open(file) as f:
        while True:
            first = f.readline().strip()
            if not first:
                break
            second = f.readline().strip()
            third = f.readline().strip()

            for letter in first:
                if letter in second:
                    if letter in third:
                        total += priority[letter]
                        break
    return total


def main():
    print("the answer is ")
    print(count("data/test_data"))
    print(count("data/real_data"))


if __name__ == "__main__":
    main()

