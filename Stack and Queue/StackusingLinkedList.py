# Node class
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Stack class
class myStack:

    def __init__(self):
        self.head = None
        self._size = 0   # keep size O(1)

    def isEmpty(self):
        return self.head is None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.isEmpty():
            return -1

        val = self.head.data
        self.head = self.head.next
        self._size -= 1
        return val

    def peek(self):
        if self.isEmpty():
            return -1
        return self.head.data

    def size(self):
        return self._size
