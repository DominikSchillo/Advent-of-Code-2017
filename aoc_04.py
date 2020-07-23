"""
    aoc_04
    https://adventofcode.com/2017/day/4
"""

from typing import List
from libs.aoc_04_lib import data_input, part_1, part_2


DATA: List[List[str]] = data_input("data/aoc_04_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 386}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 208}")
