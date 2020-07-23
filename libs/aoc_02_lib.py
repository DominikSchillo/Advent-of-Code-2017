"""aoc_02_lib"""

from typing import List


def data_input(filename: str) -> List[List[int]]:
    """"""
    with open(filename) as f:
        return [[int(element) for element in row.split("\t")] for row in f.read().splitlines()]


def part_1(data: List[List[int]]) -> int:
    """"""
    sum_1: int = 0
    for row in data:
        sum_1 += max(row) - min(row)
    return sum_1


def part_2(data: List[List[int]]) -> int:
    """"""
    sum_2: int = 0
    for row in data:
        for i, row_i in enumerate(row):
            for j, row_j in enumerate(row):
                if (row_i % row_j == 0) and (i != j):
                    sum_2 += row_i // row_j
    return sum_2
