from collections import deque

"""
Problem: Implement Stack using Queues

Implement a LIFO stack using only queue data structure.
The implemented stack should support all normal stack operations:
- push(x): Push element x onto stack
- pop(): Remove element on top of stack
- top(): Get the top element
- empty(): Check if stack is empty
"""

class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        if(len(self.queue)==0):
            return -1
        return self.queue.popleft()
        

    def top(self) -> int:
        if(len(self.queue)==0):
            return -1
        return self.queue[0]
        

    def empty(self) -> bool:
       return len(self.queue)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()