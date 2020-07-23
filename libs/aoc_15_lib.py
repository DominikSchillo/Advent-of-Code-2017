"""aoc_15_lib"""

import re
from typing import Generator, List, Pattern, Tuple


def data_input(filename: str) -> Tuple[int, int]:
    """"""
    with open(filename) as f:
        data: str = f.read()
        pattern: Pattern = re.compile(r"Generator [AB] starts with (\d+)")
        matches: List[str] = pattern.findall(data)
        return int(matches[0]), int(matches[1])


def deci_to_bin_32(number: int) -> str:
    """"""
    return str(bin(number))[2:].zfill(32)


def strings_multiplies(start: int, factor: int, divider: int, mult: int) -> Generator:
    """"""
    while True:
        start = (start * factor) % divider
        if start % mult == 0:
            yield start


def match_count(number_a: int, number_b: int, counter: int) -> int:
    """"""
    bin_string_a: str = deci_to_bin_32(number_a)
    bin_string_b: str = deci_to_bin_32(number_b)
    if bin_string_a[16:] == bin_string_b[16:]:
        counter += 1
    return counter


def constructor(starts: Tuple[int, int], factors: Tuple[int, int], divider: int, mults: Tuple[int, int], number_pairs: int) -> int:
    """"""
    iter_a = strings_multiplies(starts[0], factors[0], divider, mults[0])
    iter_b = strings_multiplies(starts[1], factors[1], divider, mults[1])

    counter: int = 0
    for _ in range(number_pairs):
        counter = match_count(next(iter_a), next(iter_b), counter)

    return counter


def part_1(starts: Tuple[int, int]) -> int:
    """"""
    factors: Tuple[int, int] = (16807, 48271)
    divider: int = 2147483647
    mults: Tuple[int, int] = (1, 1)
    number_pairs: int = 40_000_000
    return constructor(starts, factors, divider, mults, number_pairs)


def part_2(starts: Tuple[int, int]) -> int:
    """"""
    factors: Tuple[int, int] = (16807, 48271)
    divider: int = 2147483647
    mults: Tuple[int, int] = (4, 8)
    number_pairs: int = 5_000_000
    return constructor(starts, factors, divider, mults, number_pairs)
