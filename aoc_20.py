"""
    aoc_20
    https://adventofcode.com/2017/day/20
"""

from typing import List
from libs.aoc_20_lib import data_input, part_1, part_2, Particle


PARTICLES: List[Particle] = data_input("data/aoc_20_data.txt")

# Part 1
PART_1: int = part_1(PARTICLES)
print(f"Part 1: {PART_1} is {PART_1 == 157}")

# Part 2
PART_2: int = part_2(PARTICLES)
print(f"Part 2: {PART_2} is {PART_2 == 499}")
