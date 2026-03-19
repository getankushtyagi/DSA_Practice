"""
Problem: Factorial using Recursion

Calculate the factorial of a non-negative integer using recursive approach.
Factorial of n (n!) is the product of all positive integers less than or equal to n.
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""

class Factorial:
    def factorial(self,n):
        if(n<=1):
            return 1
        else:
            return n*self.factorial(n-1)
        
obj=Factorial()
print(obj.factorial(6))