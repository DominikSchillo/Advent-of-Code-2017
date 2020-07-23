"""aoc_03_lib"""

import copy
import itertools
from math import sqrt
from typing import List


def data_input(filename: str) -> int:
    """"""
    with open(filename) as f:
        return int(f.read())


def layer(point: int) -> int:
    """Calculating Layer"""
    lyr: int = 0
    if int(sqrt(point)) % 2 == 0:
        lyr = int(sqrt(point)) // 2
    elif (int(sqrt(point)) % 2 == 1) and (sqrt(point) % 1 > 0):
        lyr = (int(sqrt(point)) + 1) // 2
    elif (int(sqrt(point)) % 2 == 1) and (sqrt(point) % 1 == 0):
        lyr = (int(sqrt(point))-1) // 2
    return lyr


def calc_way_length(point: int) -> int:
    """Calculating length to CENTER"""
    layer_point: int = layer(point)
    if layer_point == 0:
        way_length: int = 0
    else:
        way_length: int = layer_point + abs(((point - (2*layer_point-1)**2) % (2*layer_point)) - layer_point)
    return way_length


def part_1(data: int) -> int:
    """"""
    return calc_way_length(data)


def sum_adjecent(grid: List[List[int]], x: int, y: int) -> int:
    """Sum of the adjecent squares (Input: x,y-coordinates, Output: Sum)"""
    sm: int = -grid[x][y]
    for i, j in itertools.product(range(3), range(3)):
        sm += grid[x-1+i][y+1-j]
    return sm


def part_2(data: int) -> int:
    """"""
    grid_size: int = 13
    diameter: int = grid_size // 2
    center: int = grid_size // 2

    grid: List[List[int]] = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    value: bool = False
    first_outside: int = 0
    grid[center][center] = 1
    for lyr in range(1, diameter - 1):
        for i in range(2 * lyr):
            sum_adj = sum_adjecent(grid, center + lyr, center - lyr + 1 + i)
            grid[center + lyr][center - lyr + 1 + i] = sum_adj
            if sum_adj > data and not value:
                first_outside = copy.copy(sum_adj)
                value = True
        for i in range(2 * lyr):
            sum_adj = sum_adjecent(grid, center + lyr - i - 1, center + lyr)
            grid[center + lyr - 1 - i][center + lyr] = sum_adj
            if sum_adj > data and not value:
                first_outside = copy.copy(sum_adj)
                value = True
        for i in range(2 * lyr):
            sum_adj = sum_adjecent(grid, center - lyr, center + lyr - 1 - i)
            grid[center - lyr][center + lyr - 1 - i] = sum_adj
            if sum_adj > data and not value:
                first_outside = copy.copy(sum_adj)
                value = True
        for i in range(2 * lyr):
            sum_adj = sum_adjecent(grid, center - lyr + 1 + i, center - lyr)
            grid[center - lyr + 1 + i][center - lyr] = sum_adj
            if sum_adj > data and not value:
                first_outside = copy.copy(sum_adj)
                value = True
    return first_outside
