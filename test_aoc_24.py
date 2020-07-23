"""test_aoc_24"""

import unittest
from typing import List, Tuple
from libs.aoc_24_lib import data_input, part_1, part_2


class TestAoC24(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[Tuple[int, int]] = data_input("data/aoc_24_data_test.txt")
        self.assertEqual(part_1(data), 31)

    def test_part_2(self):
        """"""
        data: List[Tuple[int, int]] = data_input("data/aoc_24_data_test.txt")
        self.assertEqual(part_2(data), 19)


if __name__ == '__main__':
    unittest.main()
