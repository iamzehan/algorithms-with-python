"""
Write a function, depth_first_search, that takes in the root of a binary tree and a target node to be searched.
"""

class Node:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None
def depth_first_search(root,target):
    target = Node(target)
    if root==[]:
        return False
    else:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.root==target.root:
                return True
            else:
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
        return False
    
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
