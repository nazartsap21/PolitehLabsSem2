import unittest
from src.minimum_cable_length import *


class TestMinimumCableLength(unittest.TestCase):
    def test_case_1(self):
        find_minimum_cable_length('../resources/islands_input_1.csv', '../resources/islands_output_1.csv')
        file = open('../resources/islands_output_1.csv', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, '162')

    def test_case_2(self):
        find_minimum_cable_length('../resources/islands_input_2.csv',
                                  '../resources/islands_output_2.csv')
        file = open('../resources/islands_output_2.csv', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, '33')

    def test_empty_case(self):
        find_minimum_cable_length('../resources/islands_empty_input.csv', '../resources/islands_empty_output.csv')
        file = open('../resources/islands_empty_output.csv', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, '0')


if __name__ == '__main__':
    unittest.main()
