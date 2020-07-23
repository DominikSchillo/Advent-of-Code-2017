"""
    aoc_18
    https://adventofcode.com/2017/day/18
"""

from typing import List
from libs.aoc_18_lib import data_input, part_1, part_2


INSTRUCTION_LST: List[List[str]] = data_input("data/aoc_18_data.txt")

# Part 1
PART_1: int = part_1(INSTRUCTION_LST)
print(f"Part 1: {PART_1} is {PART_1 == 2951}")

# Part 2
PART_2: int = part_2(INSTRUCTION_LST)
print(f"Part 2: {PART_2} is {PART_2 == 7366}")
