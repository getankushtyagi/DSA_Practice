""" 
Problem: Define a Binary Tree Node and Create a Binary Tree

Create a Node class to represent a binary tree node and build a binary tree
with custom values. Each node contains a value and pointers to left and right children.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Tree Structure:
#         drinks
#        /      \
#      hot      cold
#     /  \      /   \
#   tea coffee cola fanata

drinks=Node("drinks")
hot=Node("hot")
cold=Node("cold")
tea=Node("tea")
coffee=Node("coffee")
cola=Node("cola")
fanata=Node("fanata")

hot.left=tea
hot.right=coffee

cold.left=cola
cold.right=fanata

drinks.left=hot
drinks.right=cold

print(drinks.value)
print(drinks.left.value)
print(drinks.left.left.value)