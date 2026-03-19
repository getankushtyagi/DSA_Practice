"""
Problem: Maximum Depth/Height of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Solutions: Both DFS (recursive) and BFS (iterative) approaches.
"""

from collections import deque

# Example Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
# Height = 3 (levels: 1->2,3->4,5)

# with the help of dfs (recursive)
def SoltutionhDFS(node):
    if node is None:
        return 0
    
    leftHeight = SoltutionhDFS(node.left)
    rightHeight = SoltutionhDFS(node.right)
    
    return 1 + max(leftHeight, rightHeight)


# with the help of BFS
def solutionBFS(node):
    if node is None:
        return 0
        
    queue = deque([])
    height = 0
    queue.append(node)

    while len(queue):
        level_size = len(queue)
        height += 1
        
        for _ in range(level_size):
            e = queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height


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

# Call and print the height using both methods
print("Height using DFS (Recursive):", SoltutionhDFS(root))
print("Height using BFS (Iterative):", solutionBFS(root))