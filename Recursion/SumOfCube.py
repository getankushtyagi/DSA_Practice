"""
Problem: Sum of Cubes of First N Natural Numbers

Given a number n, calculate the sum of cubes of first n natural numbers using recursion.
Formula: 1³ + 2³ + 3³ + ... + n³
"""

class Solution:
    def sumOfSeries(self,n):
        #code here
        if(n<=1):
            return 1
        return n**3 + self.sumOfSeries(n-1)
obj=Solution()
print(obj.sumOfSeries(5))