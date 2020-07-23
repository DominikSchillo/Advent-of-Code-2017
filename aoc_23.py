"""
    aoc_23
    https://adventofcode.com/2017/day/23
"""

from typing import List
from libs.aoc_23_lib import data_input, part_1, part_2


INSTRUCTION_LST: List[List[str]] = data_input("data/aoc_23_data.txt")
LETTERS: str = "abcdefgh"

# Part 1
PART_1: int = part_1(INSTRUCTION_LST, LETTERS)
print(f"Part 1: {PART_1} is {PART_1 == 3969}")

# Part 2
PART_2: int = part_2(INSTRUCTION_LST, LETTERS)
print(f"Part 2: {PART_2} is {PART_2 == 917}")
