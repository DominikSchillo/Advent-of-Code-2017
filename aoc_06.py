"""
    aoc_06
    https://adventofcode.com/2017/day/6
"""

from typing import List
from libs.aoc_06_lib import data_input, part_1, part_2


DATA: List[int] = data_input("data/aoc_06_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 6681}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 2392}")
