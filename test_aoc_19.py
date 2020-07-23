"""test_aoc_19"""

import unittest
from typing import List
from libs.aoc_19_lib import data_input, part_1, part_2


class TestAoC19(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[str] = data_input("data/aoc_19_data_test.txt")
        self.assertEqual(part_1(data), "ABCDEF")

    def test_part_2(self):
        """"""
        data: List[str] = data_input("data/aoc_19_data_test.txt")
        self.assertEqual(part_2(data), 38)


if __name__ == '__main__':
    unittest.main()
