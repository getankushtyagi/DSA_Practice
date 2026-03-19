class Sol:
    def SoltutionhDFS(self,node):
        if node is None:
            return 0
        
        leftHeight = self.SoltutionhDFS(node.left)
        if(leftHeight==-1):
            return -1
        rightHeight = self.SoltutionhDFS(node.right)
        if(rightHeight==-1):
            return -1
        
        if(abs(rightHeight-leftHeight)>1):
            return -1
        
        return 1 + max(leftHeight, rightHeight)
    
    
    

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

obj=Sol()
val=obj.SoltutionhDFS(root)

if val==-1:
    print("this is not Balance Tree:")
else:
    print("this is Balance Tree:")
    
    
        