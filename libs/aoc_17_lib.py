"""aoc_17_lib"""

from typing import List, Optional, Tuple


def data_input(filename: str) -> int:
    """"""
    with open(filename) as f:
        return int(f.read())


def cycle(steps: int, lst: List[int], position: int, counter: int) -> Tuple[List[int], int, int]:
    """"""
    position = (position+steps) % (counter+1)
    counter += 1
    lst.insert(position + 1, counter)
    position += 1
    return lst, position, counter


def after_0(steps: int, position: int, counter: int, after_zero: Optional[int]) -> Tuple[int, int, Optional[int]]:
    """"""
    position = (position+steps) % (counter+1)
    counter += 1
    if position == 0:
        after_zero = counter
    position += 1
    return position, counter, after_zero


def part_1(steps: int) -> int:
    """"""
    rounds: int = 2017
    counter: int = 0
    position: int = 0
    lst: List[int] = [0]
    for _ in range(rounds):
        lst, position, counter = cycle(steps, lst, position, counter)

    return lst[position + 1]


def part_2(steps: int) -> int:
    """"""
    rounds: int = 50_000_000
    counter: int = 0
    position: int = 0
    after_zero: Optional[int] = None

    for _ in range(rounds):
        position, counter, after_zero = after_0(steps, position, counter, after_zero)

    return after_zero
