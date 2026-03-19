"""
Problem: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time O(1).
Implement the MinStack class with:
- push(val): Push element val onto stack
- pop(): Remove element on top of stack
- top(): Get the top element
- getMin(): Retrieve the minimum element in the stack
"""

class MinStack:

    def __init__(self):
        self.items=[]
        

    def push(self, val: int) -> None:
        if(len(self.items)==0):
            self.items.append([val,val])
        else:
            current_min=self.items[-1][1]
            new_min=min(current_min,val)
            self.items.append([val,new_min])
        

    def pop(self) -> None:
        if(len(self.items)==0):
            return -1
        self.items.pop()
        

    def top(self) -> int:
        if(len(self.items)==0):
            return -1
        return self.items[-1][0]
        

    def getMin(self) -> int:
        if(len(self.items)==0):
            return -1
        return self.items[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()