import unittest
from src.shortest_chess_horse_path import *


class TestShortestChessHorsePath(unittest.TestCase):
    def test_given_example(self):
        find_shortest_chess_horse_path("../resources/input.txt", "../resources/output.txt")
        file = open("../resources/output.txt")
        shortest_path = int(file.readline())
        file.close()
        self.assertEqual(shortest_path, 6)

    def test_empty_file(self):
        find_shortest_chess_horse_path("../resources/empty_input.txt", "../resources/empty_output.txt")
        file = open("../resources/empty_output.txt")
        shortest_path = int(file.readline())
        file.close()
        self.assertEqual(shortest_path, -1)


if __name__ == '__main__':
    unittest.main()
