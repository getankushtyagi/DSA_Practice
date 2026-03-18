
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
        