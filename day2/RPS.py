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
    count = 0

    with open(file) as f:
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


def count_p2(file):
    opponent = {
        "A": "R",
        "B": "P",
        "C": "S"
    }
    points = {
        "R": 1,
        "P": 2,
        "S": 3
    }
    count = 0

    with open(file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            opp, strat = line.split(" ")
            if strat == 'Y': #draw
                count += 3
                self = opponent[opp]
            elif strat == 'X': #lose
                if opponent[opp] == 'R':
                    self = 'S'
                elif opponent[opp] == 'P':
                    self = 'R'
                elif opponent[opp] == 'S':
                    self = 'P'
            elif strat == 'Z': #win
                count += 6
                if opponent[opp] == 'R':
                    self = 'P'
                elif opponent[opp] == 'P':
                    self = 'S'
                elif opponent[opp] == 'S':
                    self = 'R'

            count += points[self]

    return count


def main():
    print("the answer is ")
    print(count("data/test_data"))
    print(count("data/real_data"))
    print(count_p2("data/test_data"))
    print(count_p2("data/real_data"))


if __name__ == "__main__":
    main()

