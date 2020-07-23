"""aoc_09_lib"""

from typing import Tuple


def data_input(filename: str) -> str:
    """"""
    with open(filename) as f:
        return f.read()


def construction(data: str) -> Tuple[int, int]:
    """"""
    level: int = 0
    inside_garbage: bool = False
    sm: int = 0
    garbage_counter: int = 0
    i: int = 0

    while i < len(data):
        if data[i] == "!":
            i += 2
            continue
        elif inside_garbage:
            if data[i] == ">":
                inside_garbage = False
            else:
                garbage_counter += 1
        else:
            if data[i] == "<":
                inside_garbage = True
            else:
                if data[i] == "{":
                    level += 1
                elif data[i] == "}":
                    sm += level
                    level -= 1
        i += 1
    return sm, garbage_counter


def part_1(data: str) -> int:
    """"""
    return construction(data)[0]


def part_2(data: str) -> int:
    """"""
    return construction(data)[1]
