class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def print_tree(self, node):
        if node is None:
            return
        self.print_tree(node.left)
        print(node.value, node.priority)
        self.print_tree(node.right)

    def get_height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        else:
            return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, node):
        if node is None or node.right is None:
            return node
        y = node.right
        beta = y.left
        y.left = node
        node.right = beta
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, node):
        if node is None or node.left is None:
            return node
        y = node.left
        alpha = y.right
        y.right = node
        node.left = alpha
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, value, priority):
        if root is None:
            return Node(value, priority)
        else:
            if priority <= root.priority:
                root.left = self.insert(root.left, value, priority)
            else:
                root.right = self.insert(root.right, value, priority)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)
        if balance > 1:
            if priority <= root.left.priority:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if priority > root.right.priority:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def enqueue(self, value, priority):
        self.root = self.insert(self.root, value, priority)

    def delete_highest_priority(self, root):
        if root is None:
            return root, None

        if root.left:
            root.left, deleted_node = self.delete_highest_priority(root.left)
        else:
            deleted_node = (root.value, root.priority)
            root = root.right

        if root is None:
            return root, deleted_node

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root), deleted_node
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root), deleted_node
        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root), deleted_node
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root), deleted_node

        return root, deleted_node

    def deque(self):
        self.root, deleted_node = self.delete_highest_priority(self.root)
        return deleted_node
