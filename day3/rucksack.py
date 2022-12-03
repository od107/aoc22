def count(file):
    priority = {}

    for i in range(26):
        priority[chr(ord('a')+i)] = i + 1
        priority[chr(ord('A')+i)] = 27 + i

    total = 0

    with open(file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            length = len(line)
            first = line[:len(line)//2]
            second = line[len(line)//2:]

            for letter in first:
                if letter in second:
                    total += priority[letter]
                    break

    return total



def main():
    print("the answer is ")
    print(count("data/test_data"))
    print(count("data/real_data"))
    # print(count_p2("data/test_data"))
    # print(count_p2("data/real_data"))


if __name__ == "__main__":
    main()

