import unittest
from src.ijones import *


class TestIJones(unittest.TestCase):
    def test_first_input(self):
        ijones('../resources/ijones1.in', '../resources/ijones1.out')
        file = open('../resources/ijones1.out', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, "5")

    def test_second_input(self):
        ijones('../resources/ijones2.in', '../resources/ijones2.out')
        file = open('../resources/ijones2.out', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, "2")

    def test_third_input(self):
        ijones('../resources/ijones3.in', '../resources/ijones3.out')
        file = open('../resources/ijones3.out', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, "201684")


if __name__ == '__main__':
    unittest.main()
