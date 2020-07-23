"""aoc_24_lib"""

import re
import copy
from typing import List, Match, Optional, Pattern, Tuple


def bridge(rest_lst: List[Tuple[int, int]], used_lst: List[Tuple[int, int]], end_port: int, strength: int, strength_lst: List[int], length_lst: List[int]) -> Tuple[List[int], List[int]]:
    """"""
    for component in rest_lst:
        new_rest_lst: List[Tuple[int, int]] = rest_lst.copy()
        new_used_lst: List[Tuple[int, int]] = used_lst.copy()
        new_strength: int = copy.copy(strength)
        if end_port in component:
            new_rest_lst.remove(component)
            new_used_lst.append(component)
            new_strength += component[0] + component[1]

            new_end_port: int
            if component[0] == end_port:
                new_end_port = component[1]
            else:
                new_end_port = component[0]

            strength_lst, length_lst = bridge(new_rest_lst, new_used_lst, new_end_port, new_strength, strength_lst, length_lst)

    strength_lst.append(strength)
    length_lst.append(len(used_lst))

    return strength_lst, length_lst


def data_input(filename: str) -> List[Tuple[int, int]]:
    """"""
    with open(filename) as f:
        data: List[str] = f.read().split("\n")
        rest_lst: List[Tuple[int, int]] = []

        for component in data:
            pattern: Pattern = re.compile(r"(\d+)\/(\d+)")
            match: Optional[Match] = re.search(pattern, component)
            rest_lst.append((int(match.group(1)), int(match.group(2))))

        return rest_lst


def constructor(rest_lst: List[Tuple[int, int]]) -> Tuple[int, int]:
    """"""
    used_lst: List[Tuple[int, int]] = []
    end_port: int = 0
    strength: int = 0
    strength_lst: List[int] = []
    length_lst: List[int] = []

    strength_lst, length_lst = bridge(rest_lst, used_lst, end_port, strength, strength_lst,
                                      length_lst)
    length_strength_lst: List[Tuple[int, int]] = sorted(list(zip(length_lst, strength_lst)))

    return max(strength_lst), length_strength_lst[-1][1]


def part_1(rest_lst: List[Tuple[int, int]]) -> int:
    """"""
    return constructor(rest_lst)[0]


def part_2(rest_lst: List[Tuple[int, int]]) -> int:
    """"""
    return constructor(rest_lst)[1]
