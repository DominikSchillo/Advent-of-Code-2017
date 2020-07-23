"""
    aoc_22
    https://adventofcode.com/2017/day/22
"""

import copy
from typing import List
from libs.aoc_22_lib import data_input, part_1, part_2


START_FIELD, START_POSITION = data_input("data/aoc_22_data.txt")
START_ORIENT: List[int] = [-1, 0]

# Part 1
PART_1: int = part_1(copy.deepcopy(START_FIELD), START_POSITION, START_ORIENT)
print(f"Part 1: {PART_1} is {PART_1 == 5266}")

# Part 2
PART_2: int = part_2(START_FIELD, START_POSITION, START_ORIENT)
print(f"Part 2: {PART_2} is {PART_2 == 2511895}")
