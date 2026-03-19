"""
Problem: Square Root Without Built-in Function

Given a non-negative integer, find its square root without using any built-in square root function.
Implement it using binary search to find the largest integer whose square is less than or equal to the given number.
Return the integer part of the square root.
"""

class solution:
    def sqrt(self,num):
        if num<0:
            return None
        low,high=0 , num
        ans=0
        while(low<=high):
            mid=(low+high)//2
            
            if(mid*mid == num):
                return mid
            elif(mid*mid<num):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    
    

    
    
    
obj=solution()
print(obj.sqrt(16))