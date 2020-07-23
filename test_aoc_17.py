"""test_aoc_17"""

import unittest
from libs.aoc_17_lib import data_input, part_1


class TestAoC17(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: int = data_input("data/aoc_17_data_test.txt")
        self.assertEqual(part_1(data), 638)


if __name__ == '__main__':
    unittest.main()
