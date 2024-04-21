import unittest
from src.avl_priority_queue import *


class TestAVLPriorityTree(unittest.TestCase):
    def test_delete_max_priority_function(self):
        priority_queue = AVLTree()
        priority_queue.enqueue(4, 5)
        priority_queue.enqueue( 1, 3)
        priority_queue.enqueue(6, 1)
        priority_queue.enqueue(13, 2)
        priority_queue.enqueue(100, 7)
        priority_queue.enqueue(17, 9)
        deleted_node = priority_queue.deque()
        self.assertEqual(deleted_node, (6, 1))

    def test_equal_priority_input_data(self):
        priority_queue = AVLTree()
        priority_queue.enqueue(1, 1)
        priority_queue.enqueue(2, 2)
        priority_queue.enqueue(3, 3)
        priority_queue.enqueue(4, 4)
        priority_queue.enqueue(5, 5)
        self.assertEqual(priority_queue.root.left.value, 1)

    def test_increasing_priority_input_data(self):
        priority_queue = AVLTree()
        priority_queue.enqueue(1, 1)
        priority_queue.enqueue(11, 2)
        priority_queue.enqueue(111, 3)
        priority_queue.enqueue(1111, 4)
        priority_queue.enqueue(11111, 5)
        self.assertEqual(priority_queue.root.left.value, 1)

    def test_empty_tree(self):
        priority_queue = AVLTree()
        deleted_node = priority_queue.deque()
        self.assertEqual(deleted_node, None)


if __name__ == '__main__':
    unittest.main()
