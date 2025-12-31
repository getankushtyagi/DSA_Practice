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
                
                
obj=Solution()
print(obj.twoSumOptimize([1,3,4,2,5,6,7,8],3))
print(obj.twoSum([1,3,4,2,5,6,7,8],3))