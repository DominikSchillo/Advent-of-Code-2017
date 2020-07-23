"""test_aoc_07"""

import unittest
from typing import List
from libs.aoc_07_lib import data_input, part_1, part_2


class TestAoC07(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[str] = data_input("data/aoc_07_data_test.txt")
        self.assertEqual(part_1(data), "tknk")

    def test_part_2(self):
        """"""
        data: List[str] = data_input("data/aoc_07_data_test.txt")
        self.assertEqual(part_2(data), 60)


if __name__ == '__main__':
    unittest.main()
