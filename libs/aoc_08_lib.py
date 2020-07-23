"""aoc_08_lib"""

import operator
import re
from typing import Callable, Dict, List, Pattern, Tuple


def data_input(filename: str) -> str:
    """"""
    with open(filename) as f:
        return f.read()


def comparison(dct: Dict[str, int], str1: str, str2: str, str3: str) -> bool:
    """"""
    for k, v in dct.items():
        if str1 == k:
            value1: int = v
            break

    op_dict: Dict[str, Callable[[int, int], bool]] = {"<": operator.lt,
                                                      "<=": operator.le,
                                                      ">": operator.gt,
                                                      ">=": operator.ge,
                                                      "==": operator.eq,
                                                      "!=": operator.ne}
    return op_dict[str2](value1, int(str3))


def construction(data: str) -> Tuple[int, int]:
    """"""
    pattern: Pattern = re.compile(r"(\w+) (\w+) (-?\d+) if (\w+) ([<>=!][=]?) (-?\d+)")
    matches: List[Tuple[str]] = pattern.findall(data)
    dct: Dict[str, int] = {match[0]: 0 for match in matches}

    maximum: int = 0
    for element in matches:
        if comparison(dct, element[3], element[4], element[5]):
            for key, value in dct.items():
                if element[0] == key:
                    if element[1] == "inc":
                        dct[key] += int(element[2])
                    else:
                        dct[key] -= int(element[2])
                    entry: int = dct[key]
                    break
        maximum = max(maximum, entry)
    return max(dct.values()), maximum


def part_1(data: str) -> int:
    """"""
    return construction(data)[0]


def part_2(data: str) -> int:
    """"""
    return construction(data)[1]
