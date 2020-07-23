"""test_aoc_22"""

import unittest
from typing import List
from libs.aoc_22_lib import data_input, part_1, part_2


class TestAoC22(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        start_field, start_position = data_input("data/aoc_22_data_test.txt")
        start_orient: List[int] = [-1, 0]
        self.assertEqual(part_1(start_field, start_position, start_orient), 5587)

    def test_part_2(self):
        """"""
        start_field, start_position = data_input("data/aoc_22_data_test.txt")
        start_orient: List[int] = [-1, 0]
        self.assertEqual(part_2(start_field, start_position, start_orient), 2511944)


if __name__ == '__main__':
    unittest.main()
