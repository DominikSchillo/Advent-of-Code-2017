"""test_aoc_15"""

import unittest
from typing import Tuple
from libs.aoc_15_lib import data_input, part_1, part_2


class TestAoC15(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: Tuple[int, int] = data_input("data/aoc_15_data_test.txt")
        self.assertEqual(part_1(data), 588)

    def test_part_2(self):
        """"""
        data: Tuple[int, int] = data_input("data/aoc_15_data_test.txt")
        self.assertEqual(part_2(data), 309)


if __name__ == '__main__':
    unittest.main()
