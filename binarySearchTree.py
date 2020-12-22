# This algorithm depends on binary tree data tree representiation
# it is required to insert values as binary tree to proper working.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insertNode(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertNode(root.left, node)


def transformTreetoArray(root):
    if root:
        transformTreetoArray(root.left)
        print(root.val)
        transformTreetoArray(root.right)
