import unittest
from src.zigzag import *


class TestZigzag(unittest.TestCase):
    def test_given_array_5_on_5(self):
        result = zigzag(5, 5)
        self.assertEqual(
            result,
            [
                1,
                2,
                6,
                7,
                15,
                3,
                5,
                8,
                14,
                16,
                4,
                9,
                13,
                17,
                22,
                10,
                12,
                18,
                21,
                23,
                11,
                19,
                20,
                24,
                25,
            ],
        )

    def test_given_array_2_on_4(self):
        result = zigzag(2, 4)
        self.assertEqual(result, [1, 2, 5, 6, 3, 4, 7, 8])

    def test_single_line_array(self):
        result = zigzag(1, 6)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_single_element_array(self):
        result = zigzag(1, 1)
        self.assertEqual(result, [1])


if __name__ == "__main__":
    unittest.main()
