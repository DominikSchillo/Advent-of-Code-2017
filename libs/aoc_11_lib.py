"""aoc_11_lib"""

from typing import Dict, List, Tuple


def data_input(filename: str) -> List[str]:
    """"""
    with open(filename) as f:
        return f.read().split(",")


def direction_counter(direction: str, dictionary: Dict[str, int], coords: List[float]) -> Tuple[Dict[str, int], List[float]]:
    """"""
    dictionary[direction] += 1

    direction_dct: Dict[str, Tuple[float, float]] = {"n": (0, 1),
                                                   "ne": (1, 1 / 2),
                                                   "nw": (-1, 1 / 2),
                                                   "s": (0, -1),
                                                   "se": (1, -1 / 2),
                                                   "sw": (-1, -1 / 2)}
    new_coords = direction_dct[direction]
    coords[0] += new_coords[0]
    coords[1] += new_coords[1]
    return dictionary, coords


def construction(data: List[str]) -> Tuple[int, int]:
    """"""
    directions: List[str] = ["n", "ne", "nw", "s", "se", "sw"]
    count_dct: Dict[str, int] = {direction: 0 for direction in directions}
    coords: List[float] = [0, 0]  # (x,y)
    maximum: int = 0

    for string in data:
        count_dct, coords = direction_counter(string, count_dct, coords)
        x_distance: float = abs(coords[0])
        y_distance: float = abs(coords[1])

        if 2 * y_distance <= x_distance:
            steps: int = int(x_distance)
        else:
            steps: int = int(x_distance/2 + y_distance)  # x_distance + (y_distance - 1/2 * x_distance)

        maximum = max(maximum, steps)

    return steps, maximum


def part_1(data: List[str]) -> int:
    """"""
    return construction(data)[0]


def part_2(data: List[str]) -> int:
    """"""
    return construction(data)[1]
