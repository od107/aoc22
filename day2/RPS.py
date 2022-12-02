def count(file):
    opponent = {
        "A": "R",
        "B": "P",
        "C": "S"
    }
    myself = {
        "X": "R",
        "Y": "P",
        "Z": "S"
    }
    points = {
        "R": 1,
        "P": 2,
        "S": 3
    }

    strategy = []
    with open(file) as f:
        count = 0
        while True:
            line = f.readline().strip()
            if not line:
                break
            opp, self = line.split(" ")
            if opponent[opp] == myself[self]:
                count += 3
            elif opponent[opp] == 'R' and myself[self] == 'P'\
                    or opponent[opp] == 'P' and myself[self] == 'S'\
                    or opponent[opp] == 'S' and myself[self] == 'R':
                count += 6
            count += points[myself[self]]

    return count


def main():
    print("the answer is ")
    print(count("data/test_data"))
    print(count("data/real_data"))



if __name__ == "__main__":
    main()

