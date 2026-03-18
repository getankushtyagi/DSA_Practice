# dfs - depth first search (Recursion)
# 1.Preorder(root-left-right)
# 2.Inorder(left-root-right)
# 3.Postorder(left-right-root)

# Example Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

# preorder traversal (root-left-right) e.g value = 1,2,4,5,3

def Preorder(node):
    if(node==None):
        return
    print(node.value , end="")
    Preorder(node.left)
    Preorder(node.right)
    

# Inorder traversal (left-root-right) e.g value = 4,2,5,1,3

def Inorder(node):
    if(node==None):
        return
    Inorder(node.left)
    print(node.value , end="")
    Inorder(node.right)
    
    
# Postorder traversal (left-right-root) e.g value = 4,5,2,3,1

def Postorder(node):
    if(node==None):
        return
    Postorder(node.left)
    Postorder(node.right)
    print(node.value , end="")


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

# Call and print the traversals
print("Preorder (root-left-right): ", end="")
Preorder(root)
print()

print("Inorder (left-root-right): ", end="")
Inorder(root)
print()

print("Postorder (left-right-root): ", end="")
Postorder(root)
print()