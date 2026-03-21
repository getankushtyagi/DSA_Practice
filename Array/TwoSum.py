# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution:
    # optimal solution 
    def twoSumOptimize(self, nums,target):
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
    
    # brute force solution 
    def twoSum(self, nums,target):
       
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(target==(nums[i]+nums[j])):
                    return [i,j]
                
                
    # with the help of two pointers  if array is sorted
    def twoPointer(self,nums, target):
        i=0
        j=len(nums)-1
        if i==j or len(nums)==1:
            return nums
        
        while i<=j:
            if nums[i]+nums[j] == target:
                return [i,j]
            elif nums[i]+nums[j]<target:
                i+=1
            else:
                j-=1
        return None
            
                
                
obj=Solution()
print(obj.twoSumOptimize([1,3,4,2,5,6,7,8],3))
print(obj.twoSum([1,3,4,2,5,6,7,8],3))
print(obj.twoPointer([1,2,6,7,8],8))
print(obj.twoPointer([5,25,75],100))