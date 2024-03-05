import unittest
from src.next_in_order import *

class TestNextInOrder(unittest.TestCase):
    def test_given_tree(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.right.right = BinaryTree(20)
        root.right.right.left = BinaryTree(12)
        result = find_successor(root, root.left.right)
        self.assertEqual(result, root)