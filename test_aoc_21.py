"""test_aoc_21"""

import unittest
from libs.aoc_21_lib import data_input, part_1


class TestAoC21(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: list = data_input("data/aoc_21_data_test.txt")
        self.assertEqual(part_1(data, 2), 12)


if __name__ == '__main__':
    unittest.main()
