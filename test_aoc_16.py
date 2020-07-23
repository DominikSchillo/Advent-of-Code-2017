"""test_aoc_16"""

import unittest
from typing import List
from libs.aoc_16_lib import data_input, part_1


class TestAoC16(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[str] = data_input("data/aoc_16_data_test.txt")
        start_string: str = "abcde"
        self.assertEqual(part_1(data, start_string), "baedc")

        data: List[str] = data_input("data/aoc_16_data_test.txt")
        start_string: str = "baedc"
        self.assertEqual(part_1(data, start_string), "ceadb")


if __name__ == '__main__':
    unittest.main()
