import unittest
from src.next_in_order import *


class TestNextInOrder(unittest.TestCase):
    def test_given_tree(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.left.parent = root
        root.right.parent = root
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.left.left.parent = root.left
        root.left.right.parent = root.left
        root.right.right = BinaryTree(20)
        root.right.right.left = BinaryTree(12)
        root.right.right.parent = root.right
        root.right.right.left.parent = root.right.right
        result = find_successor(root, root.left.right)
        self.assertEqual(result, root)
