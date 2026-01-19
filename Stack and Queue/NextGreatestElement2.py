
'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number.
If it doesn't exist, return -1 for this number.
'''

class Solution:
    def nextLargerElement(self, arr):
        # code here
        n=len(arr)
        result=[-1]*n
        stack=[]
        
        for i in range(2*(n-1) , -1 , -1):
            while(len(stack) and stack[-1] <= arr[i%n]):
                stack.pop()
            if(i<n):    
                if(len(stack) !=0):
                    result[i]=stack[-1]
                
            stack.append(arr[i%n])
        return result
                
                
        
            
            
obj=Solution()
print(obj.nextLargerElement([1,2,3,4,3]))