"""
    aoc_19
    https://adventofcode.com/2017/day/19
"""

from typing import List
from libs.aoc_19_lib import data_input, part_1, part_2


DATA: List[str] = data_input("data/aoc_19_data.txt")

# Part 1
PART_1: str = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 'PVBSCMEQHY'}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 17736}")
