"""test_aoc_05"""

import unittest
from typing import List
from libs.aoc_05_lib import data_input, part_1, part_2


class TestAoC05(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[int] = data_input("data/aoc_05_data_test.txt")
        self.assertEqual(part_1(data), 5)

    def test_part_2(self):
        """"""
        data: List[int] = data_input("data/aoc_05_data_test.txt")
        self.assertEqual(part_2(data), 10)


if __name__ == '__main__':
    unittest.main()
