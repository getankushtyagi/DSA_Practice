"""
Problem: Jump Game

Given an array of non-negative integers where each element represents your maximum jump length 
at that position, determine if you can reach the last index starting from the first index.
Each element nums[i] represents the maximum length of a forward jump from index i.
"""

class JG:
    # Input: nums = [2,3,1,1,4]
    def jump(self,nums):
        last_index=len(nums)-1
        if(len(nums)==1 or len(nums)==0):
            return True
        maxi=0
        for i in range(0,last_index):
            if(i>maxi):
                return False
            current_val=i+nums[i]
            maxi = max(maxi, current_val)
            if(current_val >= last_index):
                return True
            if(nums[i]==0):
                continue
        return False
            
            
obj=JG()
print(obj.jump([0,2,3]))
print(obj.jump([3,2,1,0,4]))
print(obj.jump([3,0,8,2,0,0,1]))
# print(obj.jump([3,2,1,0,4]))
# print(obj.jump([0]))
            
            