"""
    aoc_02
    https://adventofcode.com/2017/day/2
"""

from typing import List
from libs.aoc_02_lib import data_input, part_1, part_2


DATA: List[List[int]] = data_input("data/aoc_02_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 46402}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 265}")
