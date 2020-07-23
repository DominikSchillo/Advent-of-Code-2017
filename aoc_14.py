"""
    aoc_14
    https://adventofcode.com/2017/day/14
"""

from libs.aoc_14_lib import data_input, part_1, part_2


DATA: str = data_input("data/aoc_14_data.txt")
GRID_SIZE: int = 128

# Part 1
PART_1: int = part_1(DATA, GRID_SIZE)
print(f"Part 1: {PART_1} is {PART_1 == 8226}")

# Part 2
PART_2: int = part_2(DATA, GRID_SIZE)
print(f"Part 2: {PART_2} is {PART_2 == 1128}")
