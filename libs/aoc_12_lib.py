"""aoc_12_lib"""

import re
from typing import Dict, List, Pattern, Set, Tuple


def data_input(filename: str) -> str:
    """"""
    with open(filename) as f:
        return f.read()


def id_circle(connections_dict: Dict[int, List[int]], ends: List[int], containing_id: Set[int]) -> Set[int]:
    """"""
    new_containing_id: Set[int] = containing_id.union(ends)
    if new_containing_id.difference(containing_id):
        for end in ends:
            new_containing_id = id_circle(connections_dict, connections_dict[end], new_containing_id)

    return new_containing_id


def construction(data: str) -> Tuple[int, int]:
    """"""
    connections_dict: Dict[int, List[int]] = {}
    pattern: Pattern = re.compile(r"(\d+) <-> (.+)")
    matches: List[Tuple[str, str]] = re.findall(pattern, data)
    for match in matches:
        if len(match[1]) > 1:
            connections_dict[int(match[0])] = [int(element) for element in match[1].split(", ")]
        else:
            connections_dict[int(match[0])] = [int(match[1])]

    containing_id_dict: Dict[int, Set[int]] = {}
    lst: List[int] = []
    for key, _ in connections_dict.items():
        if key not in lst:
            containing_id_dict[key] = id_circle(connections_dict, connections_dict[key], {key})
            lst += containing_id_dict[key]

    return len(containing_id_dict[0]), len(containing_id_dict)


def part_1(data: str) -> int:
    """"""
    return construction(data)[0]


def part_2(data: str) -> int:
    """"""
    return construction(data)[1]
