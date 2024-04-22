import unittest
from src.find_all_needle_occurrences import *


class TestFiniteAutomata(unittest.TestCase):
    def test_normal_case_1(self):
        result = find_needle("aaaacabaabcadacab", "acab")
        self.assertEqual(result, [3, 13])

    def test_normal_case_2(self):
        result = find_needle("ccbaacbabaabaabaaaaaba", "aaba")
        self.assertEqual(result, [9, 18])

    def test_normal_case_3(self):
        result = find_needle("aabaacaadaabaaabaa", "aaba")
        self.assertEqual(result, [0, 9, 13])

    def test_no_occurrence_case(self):
        result = find_needle("aabaacaadaabaaabaa", "guy")
        self.assertEqual(result, [])

    def test_empty_case(self):
        result = find_needle("", "")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
