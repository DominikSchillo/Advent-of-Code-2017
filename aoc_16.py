"""
    aoc_16
    https://adventofcode.com/2017/day/16
"""

from typing import List
from libs.aoc_16_lib import data_input, part_1, part_2


DATA: List[str] = data_input("data/aoc_16_data.txt")
START_STRING: str = "abcdefghijklmnop"

# Part 1
PART_1: str = part_1(DATA, START_STRING)
print(f"Part 1: {PART_1} is {PART_1 == 'doeaimlbnpjchfkg'}")

# Part 2
PART_2: str = part_2(DATA, START_STRING)
print(f"Part 2: {PART_2} is {PART_2 == 'agndefjhibklmocp'}")
