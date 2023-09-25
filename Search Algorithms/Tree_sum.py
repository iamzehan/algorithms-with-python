"""
Write a function, tree_sum, that takes in the root of a binary tree and calculates the sum of each node.
"""

class Node:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None
def tree_sum(node):
    if node == None: return 0
    return node.root + tree_sum(node.right) + tree_sum(node.left)
    
    
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       (3)
#      /   \
#   (11)   (4)
#   /  \      \
# (4)   (2)   (1)

print(tree_sum(a)) # >> 25


