def count(file):
    elves = get_elves(file)
    return max(elves)


def top3(file):
    elves = get_elves(file)
    elves.sort(reverse=True)

    return elves[0] + elves[1] + elves[2]


def get_elves(file):
    elves = []
    with open(file) as f:
        count = 0
        while True:
            line = f.readline()
            if not line:
                elves += [count]
                break
            if line != '\n':
                count += int(line.strip())
            else:
                elves += [count]
                count = 0
    return elves


def main():
    print("the answer is ")
    print(count("data/test_data"))
    print(count("data/real_data"))
    print(top3("data/test_data"))
    print(top3("data/real_data"))


if __name__ == "__main__":
    main()

