"""test_aoc_06"""

import unittest
from typing import List
from libs.aoc_06_lib import data_input, part_1, part_2


class TestAoC06(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[int] = data_input("data/aoc_06_data_test.txt")
        self.assertEqual(part_1(data), 5)

    def test_part_2(self):
        """"""
        data: List[int] = data_input("data/aoc_06_data_test.txt")
        self.assertEqual(part_2(data), 4)


if __name__ == '__main__':
    unittest.main()
