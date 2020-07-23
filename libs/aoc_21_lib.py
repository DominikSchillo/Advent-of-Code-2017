"""aoc_21_lib"""

import functools
import itertools
import re
import numpy as np
from typing import List, Match, Pattern


def create_matrix(string: str, reg_ex_raw: str):
    """"""
    pattern: Pattern = re.compile(reg_ex_raw)
    match: Match = re.search(pattern, string)
    dim_input: int = len(match.group(1))
    matrix = np.zeros((dim_input, dim_input), dtype=np.dtype(np.int16))
    for i, j in itertools.product(range(dim_input), range(dim_input)):
        matrix[i, j] = int(match.group(i + 1).zfill(dim_input)[j])
    return matrix


def compose2(f, g):
    """()"""
    return lambda x: f(g(x))


def identity(matrix):
    """(np.array -> np.array)"""
    return matrix


def rotate_90(matrix):
    """(np.array -> np.array)"""
    dim_x, dim_y = matrix.shape
    new_matrix = np.zeros((dim_y, dim_x), dtype=np.dtype(np.int16))
    for i in range(int(min(dim_x, dim_y)/2)+1):
        for y, x in itertools.product(range(i, dim_x-i), range(i, dim_y-i)):
            if y == i:
                new_matrix[x, y] = matrix[i, (dim_y-1)-x]
            elif x == dim_y-1-i:
                new_matrix[x, y] = matrix[y, i]
            elif y == dim_x-1-i:
                new_matrix[x, y] = matrix[dim_x-1-i, (dim_y-1)-x]
            elif x == i:
                new_matrix[x, y] = matrix[y, dim_y-1-i]
    return new_matrix


def rotate_180(matrix):
    """(np.array -> np.array)"""
    return compose2(rotate_90, rotate_90)(matrix)


def rotate_270(matrix):
    """(np.array -> np.array)"""
    return compose2(rotate_90, rotate_180)(matrix)


def flip_horizontal(matrix):
    """(np.array -> np.array)"""
    dim, _ = matrix.shape
    flip_matrix = rotate_90(np.eye(dim, dtype=np.dtype(np.int16)))
    return flip_matrix @ matrix


def flip_vertical(matrix):
    """(np.array -> np.array)"""
    _, dim = matrix.shape
    flip_matrix = rotate_90(np.eye(dim))
    return matrix @ flip_matrix


def in_out(ins_in_out: list, flips: list, rotations: list, matrix):
    """(list, list, list, np.array -> np.array)"""
    for flip, rotation in itertools.product(flips, rotations):
        new_matrix = compose2(flip, rotation)(matrix)
        for inpt, output in ins_in_out:
            if np.array_equal(new_matrix, inpt):
                return output


def block_matrix(matrix, height: int, width: int, i: int, j: int):
    """(np.array, int, int, int, int -> np.array)"""
    new_matrix = np.zeros((height, width))
    for x, y in itertools.product(range(height), range(width)):
        new_matrix[x, y] = matrix[x + i * height, y + j * width]
    return new_matrix


def slicing(matrix, width: int, height: int) -> list:
    """(np.array, integer, integer -> list)"""
    dim_x, dim_y = matrix.shape
    nr_slices_x: int = dim_x // height
    nr_slices_y: int = dim_y // width
    return [[block_matrix(matrix, height, width, i, j) for j in range(nr_slices_y)] for i in range(nr_slices_x)]


def gluing_horizontal2(matrix1, matrix2):
    """(np.array, np.array -> np.array)"""
    dim_x_1, dim_y_1 = matrix1.shape
    dim_x_2, dim_y_2 = matrix2.shape
    dim_y: int = dim_y_1 + dim_y_2
    if dim_x_1 == dim_x_2:
        dim_x: int = dim_x_1
        new_matrix = np.zeros((dim_x, dim_y), dtype=np.dtype(np.int16))
        for x, y in itertools.product(range(dim_x), range(dim_y)):
            if y < dim_y_1:
                new_matrix[x, y] = matrix1[x, y]
            else:
                new_matrix[x, y] = matrix2[x, y-dim_y_1]
        return new_matrix
    else:
        return "Different heights!"


def gluing_horizontal(*matrices):
    """(list -> np.array)"""
    return functools.reduce(gluing_horizontal2, matrices)


def gluing_vertical2(matrix1, matrix2):
    """(np.array, np.array -> np.array)"""
    dim_x_1, dim_y_1 = matrix1.shape
    dim_x_2, dim_y_2 = matrix2.shape
    dim_x: int = dim_x_1 + dim_x_2
    if dim_y_1 == dim_y_2:
        dim_y: int = dim_y_1
        new_matrix = np.zeros((dim_x, dim_y), dtype=np.dtype(np.int16))
        for x, y in itertools.product(range(dim_x), range(dim_y)):
            if x < dim_x_1:
                new_matrix[x, y] = matrix1[x, y]
            else:
                new_matrix[x, y] = matrix2[x-dim_x_1, y]
        return new_matrix
    else:
        return "Different widths!"


def gluing_vertical(*matrices):
    """(list -> np.array)"""
    return functools.reduce(gluing_vertical2, matrices)


def gluing(list_list_matrices: list):
    """(list -> np.array)"""
    new_list_matrices: list = []
    for list_matrices in list_list_matrices:
        new_list_matrices.append(gluing_horizontal(*list_matrices))
    return gluing_vertical(*new_list_matrices)


def iteration(ins_in_out: list, flips: list, rotations: list, matrix):
    """(list, list, list, np.array -> np.array)"""
    size, _ = matrix.shape
    slices: list
    if size % 2 == 0:
        slices = slicing(matrix, 2, 2)
    elif size % 3 == 0:
        slices = slicing(matrix, 3, 3)
    trans_slices: list = [[in_out(ins_in_out, flips, rotations, mat) for mat in mat_slice] for mat_slice in slices]
    return gluing(trans_slices)


def data_input(filename: str) -> list:
    """"""
    with open(filename) as f:
        file: str = f.read()
        file = file.replace("#", "1")
        file = file.replace(".", "0")
        file: List[str] = file.split("\n")
        input_reg_ex: str = r"(\d+)\/(\d+)\/?(\d*)? "
        output_reg_ex: str = r" (\d+)\/(\d+)\/(\d+)\/?(\d*)?"
        return [(create_matrix(dataline, input_reg_ex), create_matrix(dataline, output_reg_ex)) for dataline in file]


def constructor(instructions_in_out: list, rounds: int) -> int:
    """"""
    flips: list = [identity, flip_horizontal, flip_vertical]
    rotations: list = [identity, rotate_90, rotate_180, rotate_270]
    matrix = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]], dtype=np.dtype(np.int16))
    for _ in range(rounds):
        matrix = iteration(instructions_in_out, flips, rotations, matrix)

    return np.count_nonzero(matrix == 1)


def part_1(instructions_in_out: list, rounds: int = 5) -> int:
    """"""
    return constructor(instructions_in_out, rounds)


def part_2(instructions_in_out: list) -> int:
    """"""
    rounds: int = 18
    return constructor(instructions_in_out, rounds)
