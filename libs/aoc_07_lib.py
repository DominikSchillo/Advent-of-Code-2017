"""aoc_07_lib"""

import itertools
import re
from typing import Any, List, Match, Optional


class Tower:
    """Tower class"""

    def __init__(self, tower_str: str) -> None:
        """"""
        split: List[str] = tower_str.split(" -> ")
        x: Optional[Match] = re.search(r"(\w+) [(](\d+)[)]", split[0])
        self.name: str = str(x.group(1))
        self.weight: int = int(x.group(2))

        if len(split) > 1:
            self.subtowers_list = split[1].split(", ")
        else:
            self.subtowers_list = []

    def subtowers(self, dataset: List[str]) -> List[Any]:
        """"""
        subtowers_long: List[Tower] = []
        for subtower, string in itertools.product(self.subtowers_list, dataset):
            x: Optional[Match] = re.search(subtower + r" [(](\d+)[)]", string)
            if x is not None:
                subtowers_long.append(Tower(string))
        return subtowers_long

    def unbalanced_tower(self, dataset: List[str]) -> Optional[Any]:
        """"""
        if self.subtowers(dataset):
            subtower1 = self.subtowers(dataset)[0]
            for subtower2 in self.subtowers(dataset):
                if subtower1.total_weight(dataset) != subtower2.total_weight(dataset):
                    for subtower3 in self.subtowers(dataset):
                        if (subtower1 != subtower3) and \
                                (subtower1.total_weight(dataset) != subtower3.total_weight(dataset)):
                            unbalanced_tower = subtower1
                        else:
                            unbalanced_tower = subtower2
                    break
                else:
                    unbalanced_tower = None
        else:
            unbalanced_tower = None
        return unbalanced_tower

    def balance(self, dataset: List[str]) -> bool:
        """"""
        if self.unbalanced_tower(dataset):
            return False
        else:
            return True

    def subtowers_weight(self, dataset: List[str]) -> int:
        """"""
        sub_weight: int = 0
        for subtower in self.subtowers(dataset):
            sub_weight += subtower.total_weight(dataset)
        return sub_weight

    def total_weight(self, dataset: List[str]) -> int:
        """"""
        return self.weight+self.subtowers_weight(dataset)


def bottom_tower(dataset: List[str]) -> Tower:
    """"""
    for tower1 in dataset:
        found: bool = True
        for tower2 in dataset:
            if Tower(tower1).name in Tower(tower2).subtowers_list:
                found = False
        if found:
            bottom_tow = tower1
    return Tower(bottom_tow)


def data_input(filename: str) -> List[str]:
    """"""
    with open(filename) as f:
        return f.read().split("\n")


def part_1(data: List[str]) -> str:
    """"""
    return bottom_tower(data).name


def part_2(data: List[str]) -> int:
    """"""
    tower: Tower = bottom_tower(data)
    bal: bool = tower.balance(data)
    while not bal:
        bal = True
        for subtower in tower.unbalanced_tower(data).subtowers(data):
            if subtower.unbalanced_tower(data) is not None:
                tower = subtower
                bal = False
                break

    total_weight_list = [subtower.total_weight(data) for subtower in tower.subtowers(data)]

    return tower.unbalanced_tower(data).weight - (max(total_weight_list) - min(total_weight_list))
