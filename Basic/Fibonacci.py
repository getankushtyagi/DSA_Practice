"""
Problem: Fibonacci Sequence

Generate Fibonacci numbers using recursion.
The Fibonacci sequence is a series where each number is the sum of the two preceding ones.
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

class Fibonacci:
    def fibonacci(self,n):
        if(n<=1):
            return n
        else:
            return self.fibonacci(n-1)+self.fibonacci(n-1)
        
        
obj=Fibonacci()
val=obj.fibonacci(9)
print(val)
            