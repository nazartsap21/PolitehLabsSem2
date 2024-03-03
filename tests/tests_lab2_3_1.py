import unittest
from src.lab2_3_1 import *


class TestMaxHamsters(unittest.TestCase):
    def test_given_example_1(self):
        result = max_hamsters(7, 3, [[1, 2], [2, 2], [3, 1]])
        self.assertEqual(result, 2)

    def test_given_example_2(self):
        result = max_hamsters(19, 4, [[5, 0], [2, 2], [1, 4], [5, 1]])
        self.assertEqual(result, 3)

    def test_given_example_3(self):
        result = max_hamsters(2, 2, [[1, 50000], [1, 60000]])
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
