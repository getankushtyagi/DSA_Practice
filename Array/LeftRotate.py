"""
Problem: Left Rotate Array

Given an array and a number k, rotate the array to the left by k positions.
Elements at the beginning should move to the end while maintaining their relative order.
Example: [1,2,3,4,5] rotated left by 2 becomes [3,4,5,1,2]
"""

class LR:
    def left_rotate(self,nums,target):
        if(len(nums)<=1):
            return nums
        
        new_arr=[]
        for i in range(target):
            if(i==target):
                nums.extend(new_arr)
                return nums
            
            new_arr.append(nums.pop(0))
        return nums+new_arr


sol=LR()
print([1,2,3,4,5])
print(sol.left_rotate([1,2,3,4,5],2))
            
            
        