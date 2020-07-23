"""
    aoc_01
    https://adventofcode.com/2017/day/1
"""

from libs.aoc_01_lib import data_input, part_1, part_2


DATA: str = data_input("data/aoc_01_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 1171}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 1024}")
