"""aoc_04_lib"""

from typing import List


def data_input(filename: str) -> List[List[str]]:
    """"""
    with open(filename) as f:
        return [row.split(" ") for row in f.read().splitlines()]


def part_1(data: List[List[str]]) -> int:
    """"""
    sum_1: int = 0
    for row in data:
        valid: bool = True
        for i, row_i in enumerate(row):
            for j in range(i + 1, len(row)):
                if (row_i == row[j]) and (i != j):
                    valid = False
        if valid:
            sum_1 += 1
    return sum_1


def part_2(data: List[List[str]]) -> int:
    """"""
    sum_2: int = 0
    for row in data:
        valid: bool = True
        for i, row_i in enumerate(row):
            word_1 = row_i
            for j in range(i+1, len(row)):
                word_2 = row[j]
                if len(word_1) == len(word_2) and valid:
                    for letter in word_1:
                        if letter in word_2:
                            word_2 = word_2.replace(letter, "", 1)
                    if word_2 == "":
                        valid = False
        if valid:
            sum_2 += 1
    return sum_2
