"""test_aoc_25"""

import unittest
from libs.aoc_25_lib import data_input, part_1


class TestAoC25(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        begin_state, steps, dct = data_input("data/aoc_25_data_test.txt")
        tape_length = 10 - 1
        self.assertEqual(part_1(begin_state, steps, dct, tape_length), 3)


if __name__ == '__main__':
    unittest.main()
