import unittest
from src.minimum_cable_length import *


class TestMinimumCableLength(unittest.TestCase):
    def test_case_1(self):
        find_minimum_cable_length('../resources/islands_input.csv', '../resources/islands_output.csv')
        file = open('../resources/islands_output.csv', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, '21')

    def test_empty_case(self):
        find_minimum_cable_length('../resources/islands_empty_input.csv', '../resources/islands_empty_output.csv')
        file = open('../resources/islands_empty_output.csv', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, '0')

    def test_unconnected_graph_case(self):
        find_minimum_cable_length('../resources/islands_unconnected_input.csv', '../resources/islands_unconnected_output.csv')
        file = open('../resources/islands_unconnected_output.csv', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, '-1')


if __name__ == '__main__':
    unittest.main()
