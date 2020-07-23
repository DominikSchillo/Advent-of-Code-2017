"""
    aoc_10
    https://adventofcode.com/2017/day/10
"""

from libs.aoc_10_lib import data_input, part_1, part_2


DATA: str = data_input("data/aoc_10_data.txt")
LIST_LENGTH: int = 256

# Part 1
PART_1: int = part_1(DATA, LIST_LENGTH)
print(f"Part 1: {PART_1} is {PART_1 == 11413}")

# Part 2
PART_2: str = part_2(DATA, LIST_LENGTH)
print(f"Part 2: {PART_2} is {PART_2 == '7adfd64c2a03a4968cf708d1b7fd418d'}")
