"""aoc_05_lib"""

from typing import List


def data_input(filename: str) -> List[int]:
    """"""
    with open(filename) as f:
        return [int(number) for number in f.read().splitlines()]


def part_1(data: List[int]) -> int:
    """"""
    position: int = 0
    counter: int = 0
    new_data: List[int] = data.copy()
    while position < len(new_data):
        new_data[position] += 1
        position += new_data[position] - 1
        counter += 1
    return counter


def part_2(data: List[int]) -> int:
    """"""
    position: int = 0
    counter: int = 0
    new_data: List[int] = data.copy()
    while position < len(new_data):
        if new_data[position] >= 3:
            add: int = -1
        else:
            add: int = 1
        new_data[position] += add
        position += new_data[position] - add
        counter += 1
    return counter
