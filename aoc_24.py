"""
    aoc_24
    https://adventofcode.com/2017/day/24
"""

from typing import List, Tuple
from libs.aoc_24_lib import data_input, part_1, part_2


REST_LST: List[Tuple[int, int]] = data_input("data/aoc_24_data.txt")

# Part 1
PART_1: int = part_1(REST_LST)
print(f"Part 1: {PART_1} is {PART_1 == 1511}")

# Part 2
PART_2: int = part_2(REST_LST)
print(f"Part 2: {PART_2} is {PART_2 == 1471}")
