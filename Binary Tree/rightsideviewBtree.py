"""
Problem: Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it.
Return the values of the nodes you can see ordered from top to bottom.
The right side view contains the rightmost node at each level when viewed from the right.

Approach:
- Use level order traversal (BFS) with a queue
- For each level, capture the last (rightmost) node
- The rightmost node at each level forms the right side view

Example 1 (3 levels):
        1         <- Level 0, rightmost: 1
       / \
      2   3       <- Level 1, rightmost: 3
       \   \
        5   4     <- Level 2, rightmost: 4

Right Side View: [1, 3, 4]
Explanation: From the right side, we see nodes 1, 3, and 4.

Example 2 (5 levels):
                    1                <- Level 0: 1
                   / \
                  2   3              <- Level 1: 3
                 / \   \
                4   5   6            <- Level 2: 6
               /     \   \
              8       9   7          <- Level 3: 7
                     /
                    10               <- Level 4: 10

Right Side View: [1, 3, 6, 7, 10]
Explanation: Looking from the right, we see the rightmost node at each level.

Example 3 (4 levels - Left-skewed with some right nodes):
            1                <- Level 0: 1
           /
          2                  <- Level 1: 2
         / \
        3   4                <- Level 2: 4
       /
      5                      <- Level 3: 5

Right Side View: [1, 2, 4, 5]
Explanation: Even though the tree is left-skewed, we see the rightmost node at each level.

Example 4 (4 levels - Complete Binary Tree):
              20             <- Level 0: 20
           /      \
          8        22        <- Level 1: 22
         / \      /  \
        5   3   15   25      <- Level 2: 25
       /
      1                      <- Level 3: 1

Right Side View: [20, 22, 25, 1]
"""
from collections import deque
class sol:
    def rightSideView(self, root):
        if root is None:
            return []
        
        queue=deque()
        queue.append(root)
        result=[]
        while queue:
            level_size=len(queue)
            
            for i in range(level_size):
                node=queue.popleft()
                
                if(i==(level_size-1)):
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
        return result


# Node class definition
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# Test Case 1: Example 1 from problem (3 levels)
#        1
#       / \
#      2   3
#       \   \
#        5   4
print("Test Case 1:")
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.right = Node(5)
root1.right.right = Node(4)
obj = sol()
print("Right Side View:", obj.rightSideView(root1))
print("Expected: [1, 3, 4]\n")


# Test Case 2: Example 2 from problem (5 levels)
#                    1
#                   / \
#                  2   3
#                 / \   \
#                4   5   6
#               /     \   \
#              8       9   7
#                     /
#                    10
print("Test Case 2:")
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.right = Node(6)
root2.left.left.left = Node(8)
root2.left.right.right = Node(9)
root2.right.right.right = Node(7)
root2.left.right.right.left = Node(10)
print("Right Side View:", obj.rightSideView(root2))
print("Expected: [1, 3, 6, 7, 10]\n")


# Test Case 3: Left-skewed tree (4 levels)
#            1
#           /
#          2
#         / \
#        3   4
#       /
#      5
print("Test Case 3:")
root3 = Node(1)
root3.left = Node(2)
root3.left.left = Node(3)
root3.left.right = Node(4)
root3.left.left.left = Node(5)
print("Right Side View:", obj.rightSideView(root3))
print("Expected: [1, 2, 4, 5]\n")


# Test Case 4: Complete Binary Tree (4 levels)
#              20
#           /      \
#          8        22
#         / \      /  \
#        5   3   15   25
#       /
#      1
print("Test Case 4:")
root4 = Node(20)
root4.left = Node(8)
root4.right = Node(22)
root4.left.left = Node(5)
root4.left.right = Node(3)
root4.right.left = Node(15)
root4.right.right = Node(25)
root4.left.left.left = Node(1)
print("Right Side View:", obj.rightSideView(root4))
print("Expected: [20, 22, 25, 1]\n")


# Test Case 5: Single node tree
print("Test Case 5 (Single Node):")
root5 = Node(1)
print("Right Side View:", obj.rightSideView(root5))
print("Expected: [1]\n")


# Test Case 6: Empty tree
print("Test Case 6 (Empty Tree):")
root6 = None
print("Right Side View:", obj.rightSideView(root6))
print("Expected: []\n")


# Test Case 7: Right-skewed tree
#      1
#       \
#        2
#         \
#          3
#           \
#            4
print("Test Case 7 (Right-skewed):")
root7 = Node(1)
root7.right = Node(2)
root7.right.right = Node(3)
root7.right.right.right = Node(4)
print("Right Side View:", obj.rightSideView(root7))
print("Expected: [1, 2, 3, 4]\n")


# Test Case 8: Left-skewed tree (all left children)
#      1
#     /
#    2
#   /
#  3
# /
#4
print("Test Case 8 (Left-skewed):")
root8 = Node(1)
root8.left = Node(2)
root8.left.left = Node(3)
root8.left.left.left = Node(4)
print("Right Side View:", obj.rightSideView(root8))
print("Expected: [1, 2, 3, 4]\n")


# Test Case 9: Zigzag tree
#        1
#       /
#      2
#       \
#        3
#       /
#      4
#       \
#        5
print("Test Case 9 (Zigzag):")
root9 = Node(1)
root9.left = Node(2)
root9.left.right = Node(3)
root9.left.right.left = Node(4)
root9.left.right.left.right = Node(5)
print("Right Side View:", obj.rightSideView(root9))
print("Expected: [1, 2, 3, 4, 5]\n")