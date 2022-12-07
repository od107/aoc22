from collections import deque


def stream(file):
    stream = deque()
    with open(file) as f:
        line = f.readline()

    for i, letter in enumerate(line):
        stream.append(letter)
        if i > 12:
            if not double_char(stream):
                return i + 1
            stream.popleft()

            # if not stream.__contains__(letter):
            #     return i
    return "not found"


def double_char(stream):
    for j, char1 in enumerate(stream):
        for k, char2 in enumerate(stream):
            if j == k:
                break
            if char1 == char2:
                return True
    return False


def main():
    print("the answer is ")
    print(stream("data/test_data"))
    print(stream("data/real_data"))


if __name__ == "__main__":
    main()

