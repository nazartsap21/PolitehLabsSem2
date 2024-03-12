class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node.right:
        while node.left:
            node = node.left
        return node
    elif node.value > tree.value:
        return None
    else:
        while node.parent.right == node:
            node = node.parent
        return node.parent
