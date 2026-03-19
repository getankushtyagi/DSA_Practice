"""
Problem: Implement Lower Bound

Given a sorted array and a target value, find the lower bound - the smallest element 
in the array that is greater than or equal to the target value.
If no such element exists, return -1.
"""

class ILB:
    def lower_bound(self, nums, target):
        for x in nums:
            if x >= target:
                return x
        return -1  # target larger than all elements

obj=ILB()
print(obj.lower_bound([1,2,2,3,4,4,4,4,5,5,6,7,8,9,12],8))
            
                
            