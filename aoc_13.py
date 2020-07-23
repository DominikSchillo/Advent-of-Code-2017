"""
    aoc_13
    https://adventofcode.com/2017/day/13
"""

from typing import Dict
from libs.aoc_13_lib import data_input, part_1, part_2


DATA: Dict[int, int] = data_input("data/aoc_13_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 1840}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 3850260}")
