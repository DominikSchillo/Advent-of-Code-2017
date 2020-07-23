"""
    aoc_17
    https://adventofcode.com/2017/day/17
"""

from libs.aoc_17_lib import data_input, part_1, part_2


DATA: int = data_input("data/aoc_17_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 355}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 6154117}")
