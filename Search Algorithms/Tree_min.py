

"""
Write a function, tree_min, that takes in the root of a binary tree and calculates the minimum value of all the nodes.
"""

class Node:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None
def tree_min(node):
    if node == None: return float("inf")
    return min(node.root, tree_min(node.right),tree_min(node.left))
    
    
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

print(tree_min(a)) # >> 1
