

def part1(file):
    total = 0
    with open(file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            left, right = line.split(",")
            ll, lr = left.split("-")
            rl, rr = right.split("-")
            if int(ll) >= int(rl) and int(lr) <= int(rr) or int(ll) <= int(rl) and int(lr) >= int(rr):
                total += 1

    return total


def part2(file):
    total = 0
    with open(file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            left, right = line.split(",")
            ll, lr = left.split("-")
            rl, rr = right.split("-")
            ll, lr, rl, rr = int(ll), int(lr), int(rl), int(rr)
            if rl <= lr <= rr \
                    or rl <= ll <= rr \
                    or ll >= rl and lr <= rr \
                    or ll <= rl and lr >= rr:
                total += 1

    return total


def main():
    print("the answer is ")
    print(part1("data/test_data"))
    print(part1("data/real_data"))
    print(part2("data/test_data"))
    print(part2("data/real_data"))


if __name__ == "__main__":
    main()

