#works on LIFO principle
class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.items=[]
        self.max_size = n

    
    def isEmpty(self):
        # Check if stack is empty
        if(len(self.items)==0):
            return True
        return False

    
    def isFull(self):
        if(len(self.items)==self.max_size):
            return True
        return False

    
    def push(self, x):
        if(len(self.items)==self.max_size):
            return "stack is full"
        self.items.append(x)

    def pop(self):
        # Removes an element from the top of the stack
        if(self.isEmpty()):
            return -1
        return self.items.pop()

    def peek(self):
        # Returns the top element of the stack
        if(self.isEmpty()):
            return -1
        return self.items[-1]
