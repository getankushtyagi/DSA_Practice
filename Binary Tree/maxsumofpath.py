"""
Problem: Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
in the sequence has an edge connecting them. A node can only appear in the sequence 
at most once. The path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

class sol:
    def maxPathSum(self, root):
        self.maxi = float('-inf')  # Use -inf to handle negative values
        
        def dfs(node):  # Remove 'self' - it's a nested function
            if node is None:
                return 0
            
            ls = dfs(node.left)
            if ls < 0:
                ls = 0
                
            rs = dfs(node.right)
            if rs < 0:
                rs = 0
                
            self.maxi = max(self.maxi, ls + node.value + rs)  # Changed val to value
            
            return node.value + max(ls, rs)  # Changed val to value
        
        dfs(root)
        return self.maxi
    
    


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

obj=sol()
val=obj.maxPathSum(root)
print("maximum path value is :",val )
        



    
    
    