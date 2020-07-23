"""
    aoc_15
    https://adventofcode.com/2017/day/15
"""

from typing import Tuple
from libs.aoc_15_lib import data_input, part_1, part_2


STARTS: Tuple[int, int] = data_input("data/aoc_15_data.txt")

# Part 1
PART_1: int = part_1(STARTS)
print(f"Part 1: {PART_1} is {PART_1 == 592}")

# Part 2
PART_2: int = part_2(STARTS)
print(f"Part 2: {PART_2} is {PART_2 == 320}")
