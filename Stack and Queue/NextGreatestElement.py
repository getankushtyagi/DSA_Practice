
'''
You are given an array arr[] of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1.

'''

class Solution:
    def nextLargerElement(self, arr):
        # code here
        n=len(arr)
        result=[-1]*n
        stack=[]
        
        for i in range(n-1 , -1 , -1):
            while(len(stack) and stack[-1] <= arr[i]):
                stack.pop()
            if(len(stack) !=0):
                result[i]=stack[-1]
                
            stack.append(arr[i])
        return result
                
                
        
            
            
obj=Solution()
print(obj.nextLargerElement([1,4,1,6,0,3,10,33,42,2,6,7,3]))