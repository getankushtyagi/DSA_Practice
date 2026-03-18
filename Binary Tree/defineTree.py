class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

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