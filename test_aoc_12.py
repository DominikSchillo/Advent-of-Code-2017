"""test_aoc_12"""

import unittest
from libs.aoc_12_lib import data_input, part_1, part_2


class TestAoC12(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: str = data_input("data/aoc_12_data_test.txt")
        self.assertEqual(part_1(data), 6)

    def test_part_2(self):
        """"""
        data: str = data_input("data/aoc_12_data_test.txt")
        self.assertEqual(part_2(data), 2)


if __name__ == '__main__':
    unittest.main()
