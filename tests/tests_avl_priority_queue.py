import unittest
from src.avl_priority_queue import *


class TestAVLPriorityTree(unittest.TestCase):
    def test_delete_max_priority_function(self):
        tree = AVLTree()
        root = None
        root = tree.insert(root, 4, 5)
        root = tree.insert(root, 1, 3)
        root = tree.insert(root, 6, 1)
        root = tree.insert(root, 13, 2)
        root = tree.insert(root, 100, 7)
        root = tree.insert(root, 17, 9)
        root, deleted_node = tree.delete_highest_priority(root)
        self.assertEqual(deleted_node, (17, 9))

    def test_equal_priority_input_data(self):
        tree = AVLTree()
        root = None
        root = tree.insert(root, 1, 1)
        root = tree.insert(root, 2, 1)
        root = tree.insert(root, 3, 1)
        root = tree.insert(root, 4, 1)
        root = tree.insert(root, 5, 1)
        self.assertEqual(root.left.value, 4)

    def test_increasing_priority_input_data(self):
        tree = AVLTree()
        root = None
        root = tree.insert(root, 1, 1)
        root = tree.insert(root, 11, 2)
        root = tree.insert(root, 111, 3)
        root = tree.insert(root, 1111, 4)
        root = tree.insert(root, 11111, 5)
        self.assertEqual(root.left.value, 1111)

    def test_empty_tree(self):
        tree = AVLTree()
        root = None
        root, deleted_node = tree.delete_highest_priority(root)
        self.assertEqual(deleted_node, None)


if __name__ == '__main__':
    unittest.main()
