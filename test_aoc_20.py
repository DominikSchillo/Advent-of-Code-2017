"""test_aoc_20"""

import unittest
from typing import List
from libs.aoc_20_lib import data_input, part_1, part_2, Particle


class TestAoC20(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[Particle] = data_input("data/aoc_20_data_test_1.txt")
        self.assertEqual(part_1(data), 0)

    def test_part_2(self):
        """"""
        data: List[Particle] = data_input("data/aoc_20_data_test_2.txt")
        self.assertEqual(part_2(data), 1)


if __name__ == '__main__':
    unittest.main()
