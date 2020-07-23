"""test_aoc_02"""

import unittest
from typing import List
from libs.aoc_02_lib import data_input, part_1, part_2


class TestAoC02(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[List[int]] = data_input("data/aoc_02_data_test_1.txt")
        self.assertEqual(part_1(data), 18)

    def test_part_2(self):
        """"""
        data: List[List[int]] = data_input("data/aoc_02_data_test_2.txt")
        self.assertEqual(part_2(data), 9)


if __name__ == '__main__':
    unittest.main()
