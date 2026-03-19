"""
Problem: Top View of Binary Tree

You are given the root of a binary tree, and your task is to return its top view. 
The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Note:
- Return the nodes from the leftmost node to the rightmost node.
- If multiple nodes overlap at the same horizontal position, only the topmost (closest to the root) node is included in the view. 

Example 1:
Input: root = [1,2,3,null,4,null,5]
Output: [2,1,3]
Explanation: The nodes visible from the top view are 2, 1, and 3. Node 4 and node 5 are not visible 
from the top view because they are hidden behind node 2 and node 3 respectively.
"""

# Example Tree (4 levels):
#              1
#           /     \
#          2       3
#         / \     / \
#        4   5   6   7
#       /     \       \
#      8       9      10
#
# Top View: [8, 4, 2, 1, 3, 7, 10]
# Horizontal distances from root:
#   8: -3, 4: -2, 2: -1, 1: 0, 3: 1, 7: 2, 10: 3


# lets start the code of it 
from collections import deque
class Sol:
    
    def topView(self,root):
        if root is None:
            return None
        
        ans=[]
        queue=deque()
        queue.append((root,0)) # here we store the value and the line 
        result={}
        while queue:
            e,line = queue.popleft()
            if line not in result:
                result[line]=e.val
            if e.left:
                queue.append((e.left,line-1))
            if e.right:
                queue.append((e.right,line+1))
                
        for value in sorted(result.items()):
            ans.append(value[1])
        return ans
            
            
        




# Node class definition
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# Build the example tree with 4 levels
#              1
#           /     \
#          2       3
#         / \     / \
#        4   5   6   7
#       /     \       \
#      8       9      10

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.right.right = Node(9)
root.right.right.right = Node(10)

# Create solution object and get top view
obj = Sol()
result = obj.topView(root)
print("Top View of Binary Tree:", result)


# Example 2: A deeper tree with 5 levels
#                  20
#              /        \
#            8           22
#          /   \        /   \
#         5     3      4     25
#        / \     \           /
#       1   10   14         30
#      /
#     0
#
# Top View: [0, 1, 5, 8, 20, 22, 25, 30]

print("\n--- Example 2: Deeper Tree (5 levels) ---")
root2 = Node(20)
root2.left = Node(8)
root2.right = Node(22)
root2.left.left = Node(5)
root2.left.right = Node(3)
root2.right.left = Node(4)
root2.right.right = Node(25)
root2.left.left.left = Node(1)
root2.left.left.right = Node(10)
root2.left.right.right = Node(14)
root2.right.right.left = Node(30)
root2.left.left.left.left = Node(0)

result2 = obj.topView(root2)
print("Top View of Binary Tree:", result2)
