"""
    aoc_12
    https://adventofcode.com/2017/day/12
"""

from libs.aoc_12_lib import data_input, part_1, part_2


DATA: str = data_input("data/aoc_12_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 288}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 211}")
