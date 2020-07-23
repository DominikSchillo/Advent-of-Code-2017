"""aoc_18_lib"""

import operator
import re
from typing import Dict, List, Optional, Set, Tuple


OPS = {"add": operator.add, "mul": operator.mul, "mod": operator.mod}


def data_input(filename: str) -> List[List[str]]:
    """"""
    with open(filename) as f:
        return [row.split(" ") for row in f.read().split("\n")]


def value(string: str, dct: Dict[str, int]) -> int:
    """"""
    try:
        return int(string)
    except ValueError:
        return dct[string]


def move(lst: List[List[str]],
         index: int,
         positions: List[int],
         dcts: List[Dict[str, int]],
         queues: List[List[Optional[int]]],
         counters: List[int])\
        -> Tuple[int, List[int], List[Dict[str, int]], List[List[Optional[int]]], List[int]]:
    """"""
    if lst[positions[index]][0] == "jgz":
        if value(lst[positions[index]][1], dcts[index]) > 0:
            positions[index] += value(lst[positions[index]][2], dcts[index])
        else:
            positions[index] += 1
    elif lst[positions[index]][0] == "rcv":
        if queues[index]:
            dcts[index][lst[positions[index]][1]] = queues[index].pop(0)
            positions[index] += 1
        else:
            index ^= 1
    else:
        if lst[positions[index]][0] == "snd":
            queues[index ^ 1].append(value(lst[positions[index]][1], dcts[index]))
            counters[index] += 1
        elif lst[positions[index]][0] == "set":
            dcts[index][lst[positions[index]][1]] = value(lst[positions[index]][2], dcts[index])
        else:
            dcts[index][lst[positions[index]][1]] = OPS[lst[positions[index]][0]](
                dcts[index][lst[positions[index]][1]], value(lst[positions[index]][2], dcts[index]))

        positions[index] += 1
    return index, positions, dcts, queues, counters


def constructor(instruction_lst: List[List[str]])\
        -> Tuple[int, List[int], List[Dict[str, int]], List[List[Optional[int]]], List[int]]:
    """"""
    letters: Set[str] = {instruction[1] for instruction in instruction_lst if
                         re.search(r"\D", instruction[1])}
    dcts: List[Dict[str, int]] = [{letter: 0 for letter in letters}, {letter: 0 for letter in letters}]
    dcts[1]["p"] = 1
    positions: List[int] = [0, 0]
    queues: List[List[Optional[int]]] = [[], []]
    counters: List[int] = [0, 0]
    index: int = 0

    while index == 0 and (0 <= positions[index] < len(instruction_lst)):
        index, positions, dcts, queues, counters = move(instruction_lst, index, positions, dcts,
                                                        queues, counters)

    return index, positions, dcts, queues, counters


def part_1(instruction_lst: List[List[str]]) -> int:
    """"""
    index, _, _, queues, _ = constructor(instruction_lst)
    return queues[index][-1]


def part_2(instruction_lst: List[List[str]]) -> int:
    """"""
    index, positions, dcts, queues, counters = constructor(instruction_lst)
    while (queues != [[], []] or counters == [0, 0]) and (0 <= positions[index] < len(instruction_lst)):
        index, positions, dcts, queues, counters = move(instruction_lst, index, positions, dcts,
                                                        queues, counters)

    return counters[1]
