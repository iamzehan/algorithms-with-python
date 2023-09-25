"""
Write a function, tree_min, that takes in the root of a binary tree and calculates the minimum value of all the nodes.
"""

class Node:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None
def tree_max_sum(node):
    if node == None: return float('-inf')
    if node.left==None and node.right==None: return node.root
    max_child = max(tree_max_sum(node.left),tree_max_sum(node.right))
    return node.root + max_child
    
    
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

#       (3)
#      /   \
#   (11)   (4)
#   /  \      \
# (4)   (2)   (1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(tree_max_sum(a)) # >> 18
