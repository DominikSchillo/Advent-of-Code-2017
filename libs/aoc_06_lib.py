"""aoc_06_lib"""

from typing import List, Tuple


def data_input(filename: str) -> List[int]:
    """"""
    with open(filename) as f:
        return [int(number) for number in f.read().split("\t")]


def reallocation(seq: List[int]) -> List[int]:
    """"""
    maximum_value: int = max(seq)
    maximum_index: int = seq.index(maximum_value)
    seq[maximum_index] = 0
    counter: int = 0
    index: int = maximum_index
    while counter < maximum_value:
        index += 1
        if index > len(seq)-1:
            index = 0
        seq[index] += 1
        counter += 1
    return seq


def construction(data: List[int]) -> Tuple[int, int]:
    """"""
    seq: List[int] = data.copy()
    seqs: List[List[int]] = [data.copy()]
    in_seq: bool = False
    counter: int = 0
    while not in_seq:
        seq = reallocation(seq)
        if seq in seqs:
            in_seq = True
        seqs.append(seq.copy())
        counter += 1
    return counter, len(seqs) - 1 - seqs.index(seq)


def part_1(data: List[int]) -> int:
    """"""
    return construction(data)[0]


def part_2(data: List[int]) -> int:
    """"""
    return construction(data)[1]
