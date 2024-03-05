class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    result = []

    def inorder_traversal(root):
        if root is None:
            return
        inorder_traversal(root.left)
        result.append(root)
        inorder_traversal(root.right)
    inorder_traversal(tree)

    for i in range(len(result)):
        if i == len(result) - 1:
            break
        elif result[i] == node:
            return result[i + 1]
