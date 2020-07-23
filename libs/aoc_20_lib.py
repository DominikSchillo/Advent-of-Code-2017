"""aoc_20_lib"""

import re
from typing import List, Match, Pattern


class Particle:
    """Particle properties"""

    def __init__(self, string, index: int) -> None:
        """"""
        pattern: Pattern = re.compile(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>")
        matches: Match = pattern.search(string)
        self.index: int = index
        self.pos: List[int] = [int(matches.group(i)) for i in range(1, 4)]
        self.vel: List[int] = [int(matches.group(i)) for i in range(4, 7)]
        self.acc: List[int] = [int(matches.group(i)) for i in range(7, 10)]

    def move(self) -> None:
        """"""
        for i in range(3):
            self.vel[i] += self.acc[i]
        for i in range(3):
            self.pos[i] += self.vel[i]

    def distance(self, n: int) -> int:
        """"""
        self.pos = [self.pos[i] + n * (self.vel[i] + 0.5 * self.acc[i]) + n ** 2 * 0.5 * self.acc[i]
                    for i in range(3)]
        return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        # vel_n = vel0+ n * acc0
        # pos_n = pos0 + n * vel0 + n * (n + 1) / 2 * acc0 = pos0 + n * (vel0 + 1 / 2 acc0) + n ^ 2 * 1 / 2 acc0


def data_input(filename: str) -> List[Particle]:
    """"""
    with open(filename) as f:
        return [Particle(datastring, index) for index, datastring in enumerate(f.read().split("\n"))]


def part_1(particles: List[Particle]) -> int:
    """"""
    acc_min: int = 0
    acc_min_list: List[Particle] = []

    for particle in particles:
        acc_sum = abs(particle.acc[0]) + abs(particle.acc[1]) + abs(particle.acc[2])
        if acc_min > acc_sum or particle.index == 0:
            acc_min = acc_sum
            acc_min_list = [particle]
        elif acc_min >= acc_sum:
            acc_min_list.append(particle)

    vel_min: int = 0
    vel_min_list: List[Particle] = []

    for particle in acc_min_list:
        vel_sum = abs(particle.vel[0]) + abs(particle.vel[1]) + abs(particle.vel[2])
        if vel_min > vel_sum or particle.index == min(
                [particle.index for particle in acc_min_list]):
            vel_min = vel_sum
            vel_min_list = [particle]
        elif vel_min >= vel_sum:
            vel_min_list.append(particle)

    return vel_min_list[0].index


def part_2(particles: List[Particle]) -> int:
    """"""
    new_particles: List[Particle] = []

    for particle1 in particles:
        for particle2 in particles:
            if particle1.pos == particle2.pos and particle1 != particle2:
                break
        else:
            new_particles.append(particle1)

    for _ in range(100):
        particles = new_particles.copy()
        new_particles = []
        for particle in particles:
            particle.move()
        for particle1 in particles:
            for particle2 in particles:
                if particle1.pos == particle2.pos and particle1 != particle2:
                    break
            else:
                new_particles.append(particle1)

    return len(new_particles)
