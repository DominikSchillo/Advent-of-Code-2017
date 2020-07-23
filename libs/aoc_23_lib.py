"""aoc_23_lib"""

import operator
from typing import Dict, List
from libs.aoc_18_lib import value


OPS = {"sub": operator.sub, "mul": operator.mul}


class ExperimentalCoprocessor:
    """"""
    
    def __init__(self, instruction_lst: List[List[str]], position: int, dct: Dict[str, int]) -> None:
        """"""
        self.instruction_lst: List[List[str]] = instruction_lst
        self.position: int = position
        self.dct: Dict[str, int] = dct

    def move(self) -> None:
        """(list, integer, list, dict, list, list -> integer, list, dict, list, list)"""
        if self.instruction_lst[self.position][0] == "jnz":
            if value(self.instruction_lst[self.position][1], self.dct) != 0:
                self.position += value(self.instruction_lst[self.position][2], self.dct)
            else:
                self.position += 1
        else:
            if self.instruction_lst[self.position][0] == "set":
                self.dct[self.instruction_lst[self.position][1]] = value(self.instruction_lst[self.position][2], self.dct)
            else:
                self.dct[self.instruction_lst[self.position][1]] = OPS[self.instruction_lst[self.position][0]](
                    self.dct[self.instruction_lst[self.position][1]], value(self.instruction_lst[self.position][2], self.dct))

            self.position += 1

    def start(self) -> None:
        """Initial set-up[1:8] (list, integer, dict -> integer, dict)"""
        while self.position < 8:
            self.move()

    def loop(self) -> None:
        """Loop[9:32] (integer, dict -> integer, dict)"""
        self.dct["f"] = 1
        # dct["e"] = dct["b"]
        # dct["d"] = dct["b"]
        if not is_prime(self.dct["b"]):
            self.dct["f"] = 0
        if self.dct["f"] == 0:
            self.dct["h"] -= -1
        self.dct["g"] = self.dct["b"] - self.dct["c"]
        self.position += 19
        if self.dct["g"] == 0:
            self.position += 4
        else:
            self.dct["b"] -= -17
            self.position -= 19

    def run(self) -> None:
        # Initializing
        self.start()
        # Getting into the loop for the first time
        self.move()
        self.move()
        self.move()

        while self.position < len(self.instruction_lst):
            self.loop()


def is_prime(n: int) -> bool:
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def data_input(filename: str) -> List[List[str]]:
    """"""
    with open(filename) as f:
        return [row.split(" ") for row in f.read().split("\n")]


def part_1(instruction_lst: List[List[str]], letters: str) -> int:
    """"""
    position: int = 0
    dct: Dict[str, int] = {letter: 0 for letter in letters}
    experimental_coprocessor: ExperimentalCoprocessor = ExperimentalCoprocessor(instruction_lst, position, dct)
    mul_counter: int = 0

    while experimental_coprocessor.position < len(instruction_lst):
        if instruction_lst[experimental_coprocessor.position][0] == "mul":
            mul_counter += 1
        experimental_coprocessor.move()

    return mul_counter


def part_2(instruction_lst: List[List[str]], letters: str) -> int:
    """"""
    position: int = 0
    dct: Dict[str, int] = {letter: 0 for letter in letters}
    dct["a"] = 1
    experimental_coprocessor: ExperimentalCoprocessor = ExperimentalCoprocessor(instruction_lst, position, dct)

    experimental_coprocessor.run()

    return dct["h"]
