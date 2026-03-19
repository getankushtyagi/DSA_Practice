"""
Problem: Implement Queue using Stacks

Implement a FIFO queue using only two stacks.
The implemented queue should support all normal queue operations:
- push(x): Push element x to the back of queue
- pop(): Remove element from front of queue
- peek(): Get the front element
- empty(): Check if queue is empty
"""

class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def push(self, x: int) -> None:

        while(self.stack1):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while(self.stack2):
            self.stack1.append(self.stack2.pop())
        

    def pop(self) -> int:
        if(len(self.stack1)==0):
            return -1
        return self.stack1.pop()
        

    def peek(self) -> int:
        if(len(self.stack1)==0):
            return -1
        return self.stack1[-1]
        

    def empty(self) -> bool:
        return len(self.stack1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()