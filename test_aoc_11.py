"""test_aoc_11"""

import unittest
from typing import List
from libs.aoc_11_lib import data_input, part_1


class TestAoC11(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[str] = data_input("data/aoc_11_data_test_1.txt")
        self.assertEqual(part_1(data), 3)

        data: List[str] = data_input("data/aoc_11_data_test_2.txt")
        self.assertEqual(part_1(data), 0)

        data: List[str] = data_input("data/aoc_11_data_test_3.txt")
        self.assertEqual(part_1(data), 2)

        data: List[str] = data_input("data/aoc_11_data_test_4.txt")
        self.assertEqual(part_1(data), 3)


if __name__ == '__main__':
    unittest.main()
