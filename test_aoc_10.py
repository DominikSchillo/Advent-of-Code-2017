"""test_aoc_10"""

import unittest
from libs.aoc_10_lib import data_input, part_1, part_2


class TestAoC10(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: str = data_input("data/aoc_10_data_test.txt")
        self.assertEqual(part_1(data, 5), 12)

    def test_part_2(self):
        """"""
        data: str = ""
        self.assertEqual(part_2(data), "a2582a3a0e66e6e86e3812dcb672a272")

        data: str = "AoC 2017"
        self.assertEqual(part_2(data), "33efeb34ea91902bb2f59c9920caa6cd")

        data: str = "1,2,3"
        self.assertEqual(part_2(data), "3efbe78a8d82f29979031a4aa0b16a9d")

        data: str = "1,2,4"
        self.assertEqual(part_2(data), "63960835bcdc130f0b66d7ff4f6a5a8e")


if __name__ == '__main__':
    unittest.main()
