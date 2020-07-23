"""aoc_25_lib"""

import math
import re
from typing import Dict, List, Pattern, Tuple


def move(dct: Dict[str, Tuple[Tuple[int, int, str], Tuple[int, int, str]]], tape: List[int],
         cursor: int, state: str) -> Tuple[List[int], int, str]:
    """"""
    tape_cursor: int = tape[cursor]
    tape[cursor] = dct[state][tape_cursor][0]
    cursor += dct[state][tape_cursor][1]
    state = dct[state][tape_cursor][2]
    return tape, cursor, state


def direction(string: str) -> int:
    """"""
    if string == "left":
        return -1
    elif string == "right":
        return 1


def data_input(filename: str) -> Tuple[str, int, Dict[str, Tuple[Tuple[int, int, str], Tuple[int, int, str]]]]:
    """"""
    with open(filename) as f:
        file: str = f.read()

        begin_pattern: Pattern = re.compile(r"Begin in state (\w)")
        begin_state: str = re.search(begin_pattern, file).group(1)

        steps_pattern: Pattern = re.compile(r"Perform a diagnostic checksum after (\d+) steps.")
        steps: int = int(re.search(steps_pattern, file).group(1))

        dct_pattern: Pattern = re.compile(r"In state (\w):\n  If the current value is 0:\n    - Write the value (\d).\n    - Move one slot to the (left|right).\n    - Continue with state (\w).\n  If the current value is 1:\n    - Write the value (\d).\n    - Move one slot to the (left|right).\n    - Continue with state (\w).")
        dct_findall: List[Tuple[str, str, str, str, str, str]] = re.findall(dct_pattern, file)
        dct = {tup[0]: ((int(tup[1]), direction(tup[2]), tup[3]), (int(tup[4]), direction(tup[5]), tup[6])) for tup in dct_findall}

        return begin_state, steps, dct


def part_1(state: str, steps: int, dct: Dict[str, Tuple[Tuple[int, int, str], Tuple[int, int, str]]], tape_length: int) -> int:
    """"""
    tape: List[int] = [0 for _ in range(tape_length)]
    cursor: int = math.ceil(tape_length / 2) - 1
    counter: int = 0

    while counter < steps:
        tape, cursor, state = move(dct, tape, cursor, state)
        counter += 1

    return tape.count(1)
