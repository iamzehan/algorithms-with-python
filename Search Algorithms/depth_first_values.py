"""
Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
def depth_first_search(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

depth_first_search(a)


# © This code block was taken from Structy.net (Free Code Camp Tutorial: Binary Tree Algorithms for Technical Interviews)
