# bfs - level order traversal (breadth first search)
# worked on queue - processes nodes level by level

from collections import deque

# Example Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

def bfs(node):
    if node is None:
        return []
    
    result = []
    queue = deque([node])
    
    while queue:
        current = queue.popleft()  # Remove from front of queue
        result.append(current.value)  # Process current node
        
        # Add children to queue (left to right)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result


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

# Call and print the BFS traversal
print("BFS (Level Order): ", end="")
result = bfs(root)
print(result)  # Output: [1, 2, 3, 4, 5]




# # Using list (SLOW for large trees)
# queue = [1, 2, 3, 4, 5]
# queue.pop(0)  # Removes 1, but shifts [2,3,4,5] left - O(n)

# # Using deque (FAST)
# from collections import deque
# queue = deque([1, 2, 3, 4, 5])
# queue.popleft()  # Removes 1 instantly - O(1)