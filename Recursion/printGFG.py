"""
Problem: Print String N Times using Recursion

Given a string "GFG" and a number n, print the string n times using recursion.
Demonstrates basic recursive function calls with a base case.
"""

class Solution:
    def printGfg(self, n):
        
        if(n==0):
            return
        print("GFG",end=" ")
        self.printGfg(n-1)
        
obj=Solution()
obj.printGfg(10)