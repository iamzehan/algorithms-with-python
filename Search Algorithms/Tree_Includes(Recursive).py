"""
Write a function, depth_first_search, that takes in the root of a binary tree and a target node to be searched.
"""

class Node:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None
def depth_first_search(root,target):
    if root == None: return False
    if root.root == target: return True 
    return depth_first_search(root.right, target) or depth_first_search(root.left, target)
    
    
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

print(depth_first_search(a, 'e')) # >> True 
print(depth_first_search(a, 'j')) # >> False
