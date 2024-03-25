import unittest
from src.shortest_chess_horse_path import *


class TestShortestChessHorsePath(unittest.TestCase):
    def test_given_example(self):
        start_position, end_position, board_size = get_input("../resources/input.txt")
        write_output("../resources/output.txt", shortest_chess_horse_path(start_position, end_position, board_size))
        file = open("../resources/output.txt")
        shortest_path = int(file.readline())
        file.close()
        self.assertEqual(shortest_path, 6)

    def test_empty_file(self):
        start_position, end_position, board_size = get_input("../resources/empty_input.txt")
        write_output("../resources/empty_output.txt", shortest_chess_horse_path(start_position, end_position, board_size))
        file = open("../resources/empty_output.txt")
        shortest_path = int(file.readline())
        file.close()
        self.assertEqual(shortest_path, -1)


if __name__ == '__main__':
    unittest.main()
