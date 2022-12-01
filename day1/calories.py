def count(file):
    elves = []
    with open(file) as f:
        count = 0
        while True:
            line = f.readline()
            if not line:
                break
            if line != '\n':
                count += int(line.strip())
            else:
                elves += [count]
                count = 0

    return max(elves)


def main():
    print("the answer is ")
    print(count("data/test_data"))
    print(count("data/real_data"))


if __name__ == "__main__":
    main()

