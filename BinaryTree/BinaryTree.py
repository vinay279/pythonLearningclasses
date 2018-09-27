'''Construct completely balanced binary trees
In a completely balanced binary tree,
the following property holds for every node: The number of nodes in its left subtree and the number of nodes
in its right subtree are almost equal, which means their difference is not greater than one.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.rootNode = None


    def getNode(self):


