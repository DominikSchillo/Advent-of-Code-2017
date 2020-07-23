"""test_aoc_14"""

import unittest
from libs.aoc_14_lib import data_input, part_1, part_2


class TestAoC14(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: str = data_input("data/aoc_14_data_test_1.txt")
        self.assertEqual(part_1(data), 8108)

    def test_part_2(self):
        """"""
        data: str = data_input("data/aoc_14_data_test_1.txt")
        self.assertEqual(part_2(data), 1242)


if __name__ == '__main__':
    unittest.main()
