"""aoc_14_lib"""

import itertools
from typing import Dict, List, Tuple, Optional
from libs.aoc_lib import knot_hash


def data_input(filename: str) -> str:
    """"""
    with open(filename) as f:
        return f.read()


def hextobin(string: str) -> str:
    """(From https://stackoverflow.com/questions/1425493/convert-hex-to-binary)"""
    return bin(int(string, 16))[2:].zfill(len(string) * 4)  # 16: hexa, 4=log2(16)


def adjacent(grid_size: int, i: int, j: int) -> List[Tuple[int, int]]:
    """"""
    if i == 0:
        if j == 0:
            lst = [(i+1, j), (i, j+1)]
        elif j == grid_size-1:
            lst = [(i+1, j), (i, j-1)]
        else:
            lst = [(i+1, j), (i, j+1), (i, j-1)]
    elif i == grid_size-1:
        if j == 0:
            lst = [(i - 1, j), (i, j + 1)]
        elif j == grid_size - 1:
            lst = [(i - 1, j), (i, j - 1)]
        else:
            lst = [(i - 1, j), (i, j + 1), (i, j - 1)]
    else:
        if j == 0:
            lst = [(i - 1, j), (i, j + 1), (i+1, j)]
        elif j == grid_size - 1:
            lst = [(i - 1, j), (i, j - 1), (i+1, j)]
        else:
            lst = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return lst


def propagation(dct: Dict[int, List[Tuple[int, int]]], key: int, grid_size: int,
                grid: List[str], i: int, j: int) \
        -> Dict[int, List[Tuple[int, int]]]:
    """"""
    for point in adjacent(grid_size, i, j):
        if grid[point[0]][point[1]] == "1" and point not in dct[key]:
            dct[key].append(point)
            dct = propagation(dct, key, grid_size, grid, point[0], point[1])
    return dct


def grouping(grid_size: int, grid: List[str], dct: Dict[int, List[Tuple[int, int]]]) \
        -> Dict[int, List[Tuple[int, int]]]:
    """"""
    for i, j in itertools.product(range(grid_size), range(grid_size)):
        if grid[i][j] == "1":
            new_key: Optional[int] = None
            for key, lst in dct.items():
                if (i, j) in lst:
                    new_key = key
                    break
            if new_key is None:
                new_key = len(dct)
                dct[new_key] = [(i, j)]
                dct = propagation(dct, new_key, grid_size, grid, i, j)
    return dct


def construction(data: str, grid_size: int) -> List[str]:
    """"""
    know_hashs: List[str] = []
    know_hashs_binary: List[str] = []
    for i in range(grid_size):
        know_hashs.append(knot_hash(data + "-{}".format(i)))
        know_hashs_binary.append(hextobin(know_hashs[-1]))
    return know_hashs_binary


def part_1(data: str, grid_size: int = 128) -> int:
    """"""
    know_hashs_binary: List[str] = construction(data, grid_size)
    counter: int = 0
    for knot_hash in know_hashs_binary:
        counter += knot_hash.count("1")
    return counter


def part_2(data: str, grid_size: int = 128) -> int:
    """"""
    grid: List[str] = construction(data, grid_size)
    dct: Dict[int, List[Tuple[int, int]]] = {}
    dct = grouping(grid_size, grid, dct)
    return len(dct)
