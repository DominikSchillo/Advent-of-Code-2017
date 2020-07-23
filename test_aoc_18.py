"""test_aoc_18"""

import unittest
from typing import List
from libs.aoc_18_lib import data_input, part_1, part_2


class TestAoC18(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[List[str]] = data_input("data/aoc_18_data_test_1.txt")
        self.assertEqual(part_1(data), 4)

    def test_part_2(self):
        """"""
        data: List[List[str]] = data_input("data/aoc_18_data_test_2.txt")
        self.assertEqual(part_2(data), 3)


if __name__ == '__main__':
    unittest.main()
