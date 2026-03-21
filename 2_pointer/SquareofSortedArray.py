# this is a two pointer problem where we have to find the square of the sorted array and return the sorted array of the squares.
#their time complexity is O(n) and space complexity is O(n) as we are using an extra array to store the squares of the elements in the input array.


from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        arr=[0]*len(nums)
        
        i=0
        j=len(nums)-1
        idx=len(nums)-1
        
        while(i<j):
            if(nums[i]<nums[j]):
                arr[idx]=nums[j]
                idx-=1
                j-=1
            else:
                arr[idx]=nums[i]
                idx-=1
                i+=1
        return arr
        
        
obj=Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))