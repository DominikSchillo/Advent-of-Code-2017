"""
    aoc_25
    https://adventofcode.com/2017/day/25
"""

from libs.aoc_25_lib import data_input, part_1


BEGIN_STATE, STEPS, DCT = data_input("data/aoc_25_data.txt")
TAPE_LENGTH: int = 10_000_000 - 1

# Part 1
PART_1: int = part_1(BEGIN_STATE, STEPS, DCT, TAPE_LENGTH)
print(f"Part 1: {PART_1} is {PART_1 == 2725}")
