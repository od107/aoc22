from day1.calories import *


def test_part1():
    assert count("day1/data/test_data") == 24000
    assert count("day1/data/real_data") == 74711


def test_part2():
    assert top3("day1/data/test_data") == 45000
    assert top3("day1/data/real_data") == 209481
