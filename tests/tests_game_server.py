import unittest
from src.game_server import *


class TestGameServer(unittest.TestCase):
    def test_given_example_1(self):
        game_ping('../resources/gamsrv_1.in', '../resources/gamsrv_1.out')
        file = open('../resources/gamsrv_1.out', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 100)

    def test_given_example_2(self):
        game_ping('../resources/gamsrv_2.in', '../resources/gamsrv_2.out')
        file = open('../resources/gamsrv_2.out', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 10)

    def test_given_example_3(self):
        game_ping('../resources/gamsrv_3.in', '../resources/gamsrv_3.out')
        file = open('../resources/gamsrv_3.out', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 10000000)

    def test_empty_input(self):
        game_ping('../resources/gamsrv_empty.in', '../resources/gamsrv_empty.out')
        file = open('../resources/gamsrv_empty.out', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
