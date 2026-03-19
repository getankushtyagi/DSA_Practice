"""
Problem: Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes 
in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

class soltuion:
    def diameterBtree(self,root):
        self.diameter=0
        
        def dfs(node):
            if node is None:
                return 0
            
            left=dfs(node.left)
            right=dfs(node.right)
            
            self.diameter=max(self.diameter,left+right)
            return 1+max(left,right)
        dfs(root)
        return self.diameter




# Node class definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Build the example tree
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

obj=soltuion()
print("maximum diameter is :", obj.diameterBtree(root))
        