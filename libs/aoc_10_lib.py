"""aoc_10_lib"""

from typing import List
from libs.aoc_lib import knotting, knot_hash

def data_input(filename: str) -> str:
    """"""
    with open(filename) as f:
        return f.read()


def part_1(data: str, list_length: int = 256) -> int:
    """"""
    lengths: List[int] = [int(number) for number in data.split(",")]
    lst: List[int] = [n for n in range(list_length)]
    current_position: int = 0
    skip_size: int = 0
    string: List[int] = knotting(lengths, lst, current_position, skip_size, list_length)[0]
    return string[0]*string[1]


def part_2(data: str, list_length: int = 256) -> str:
    """"""
    return knot_hash(data, list_length).lower()
