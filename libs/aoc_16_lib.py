"""aoc_16_lib"""

import re
from typing import List, Match, Pattern


class ProgramGroup:
    """"""

    def __init__(self, string: str) -> None:
        """"""
        self.string: str = string

    def spin(self, position: int) -> str:
        """"""
        return self.string[-position:] + self.string[:len(self.string)-position]
    
    def exchange(self, position_1: int, position_2: int) -> str:
        """"""
        lst = list(self.string)
        lst[position_1], lst[position_2] = lst[position_2], lst[position_1]
        return "".join(lst)
    
    def partner(self, name_1: str, name_2: str) -> str:
        """"""
        return self.exchange(self.string.index(name_1), self.string.index(name_2))
    
    def movement(self, move: str) -> None:
        """"""
        pattern_spin: Pattern = re.compile(r"s(\d+)")
        match_spin: Match = re.search(pattern_spin, move)
    
        pattern_exchange: Pattern = re.compile(r"x(\d+)/(\d+)")
        match_exchange: Match = re.search(pattern_exchange, move)
    
        pattern_partner: Pattern = re.compile(r"p(\w+)/(\w+)")
        match_partner: Match = re.search(pattern_partner, move)
    
        if match_spin:
            self.string = self.spin(int(match_spin.group(1)))
        elif match_exchange:
            self.string = self.exchange(int(match_exchange.group(1)), int(match_exchange.group(2)))
        elif match_partner:
            self.string = self.partner(match_partner.group(1), match_partner.group(2))
    
    def dance(self, moves: List[str]) -> None:
        """"""
        for move in moves:
            self.movement(move)


def data_input(filename: str) -> List[str]:
    """"""
    with open(filename) as f:
        return f.read().split(",")
    

def part_1(data: List[str], start_string: str) -> str:
    """"""
    program_group: ProgramGroup = ProgramGroup(start_string)
    program_group.dance(data)
    return program_group.string


def part_2(data: List[str], start_string: str) -> str:
    """"""
    rounds: int = 1_000_000_000
    program_group: ProgramGroup = ProgramGroup(start_string)

    counter: int = 0
    while program_group.string != start_string or counter == 0:
        program_group.dance(data)
        counter += 1

    for _ in range(rounds % counter):
        program_group.dance(data)

    return program_group.string
