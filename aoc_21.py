"""
    aoc_21
    https://adventofcode.com/2017/day/21
"""

from libs.aoc_21_lib import data_input, part_1, part_2


INSTRUCTIONS_IN_OUT: list = data_input("data/aoc_21_data.txt")

# Part 1
PART_1: int = part_1(INSTRUCTIONS_IN_OUT)
print(f"Part 1: {PART_1} is {PART_1 == 150}")

# Part 2
PART_2: int = part_2(INSTRUCTIONS_IN_OUT)
print(f"Part 2: {PART_2} is {PART_2 == 2606275}")
