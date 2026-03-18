# bfs - breadth firsr search
# dfs - depth firsr search (Recursion)
# 1.Preorder(root-left-right)
# 2.Inorder(left-root-right)
# 3.Postorder(left-right-root)

# Example Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

# preorder traversal (left-root-right) e.g value = 1,2,4,5,3

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
    
    
# Postorder traversal (left-root-right) e.g value = 4,2,5,1,3

def Postorder(node):
    if(node==None):
        return
    print(node.value , end="")
    Postorder(node.right)
    Postorder(node.left)