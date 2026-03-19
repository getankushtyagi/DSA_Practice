"""
Problem: Bottom View of Binary Tree

Given a binary tree, return the bottom view of the tree from left to right.
The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.
For each horizontal distance, we only want the bottommost node (the node at the lowest level).

Approach:
- Use level order traversal (BFS) with a queue
- Track horizontal distance (HD) for each node
- For each horizontal distance, keep updating with nodes at deeper levels
- The last node encountered at each HD will be in the bottom view

Example Tree (5 levels):
                    1 (HD: 0)
                   / \
                  2   3 (HD: -1, +1)
                 / \   \
                4   5   6 (HD: -2, 0, +2)
               /     \   \
              8       9   7 (HD: -3, +1, +3)
                     /
                    10 (HD: 0)

Horizontal Distance (HD) explanation:
- Root node has HD = 0
- Left child has HD = parent_HD - 1
- Right child has HD = parent_HD + 1

Bottom View for above tree:
HD:  -3  -2  -1   0   +1  +2  +3
Node: 8   4   2  10   9   6   7

Output: [8, 4, 2, 10, 9, 6, 7]

Another Example (4 levels):
            20
           /  \
         8     22
        / \      \
      5    3     25
          / \
         10 14

Bottom View: [5, 10, 3, 14, 25]
"""

from collections import deque
class sol:

    def bottomViwe(self,root):
        if root is None:
            return None
        
        ans=[]
        queue=deque()
        queue.append((root,0))
        result={}
        
        while queue:
            e,line = queue.popleft()
            result[line]=e.val
            
            # if line in result:
            #     result[line]
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
obj = sol()
result = obj.bottomViwe(root)
print("bottom", result)


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

result2 = obj.bottomViwe(root2)
print("bottom View of Binary Tree:", result2)
