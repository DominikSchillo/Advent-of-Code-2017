"""aoc_13_lib"""

import re
from typing import Any, Dict, Iterator, List, Pattern, Tuple, Union


def data_input(filename: str) -> Dict[int, int]:
    """"""
    with open(filename) as f:
        file = f.read()
        pattern: Pattern = re.compile(r"(\d+): (\d+)")
        matches: Iterator = re.finditer(pattern, file)
        return {int(match.group(1)): int(match.group(2)) for match in matches}


def movement(dct: Dict[int, int], depth: int, ran: int, deeper: bool) -> Tuple[int, bool]:
    """"""
    if deeper:
        ran += 1
    else:
        ran -= 1

    if ran == 1:
        deeper = True
    elif ran == dct[depth]:
        deeper = False
    return ran, deeper


def drive_through(dct: Dict[int, int], positions: Dict[int, List[Any]], packet_position_delay: int)\
        -> int:
    """"""
    packet_position: int = -packet_position_delay
    severity: int = 0
    for _ in range(max(dct)+1+packet_position_delay):
        if packet_position in dct and positions[packet_position][0] == 1:
            if packet_position != 0:
                severity += packet_position * dct[packet_position]
        for depth, lst in positions.items():
            positions[depth] = list(movement(dct, depth, *lst))
        packet_position += 1
    return severity


def part_1(data: Dict[int, int]) -> int:
    """"""
    packet_position_delay: int = 0
    positions: Dict[int, List[Union[int, bool]]] = {key: [1, True] for key in data.keys()}
    return drive_through(data, positions, packet_position_delay)


def part_2(data: Dict[int, int]) -> int:
    """"""
    packet_position_delay: int = -1
    clear_path: bool = False

    while not clear_path:
        packet_position_delay += 1
        clear_path = True
        for depth, rng in data.items():
            cycle: int = 2 * rng - 2
            if (packet_position_delay + depth) % cycle == 0:
                clear_path = False
                break

    return packet_position_delay
