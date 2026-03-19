#brute force aaproach
"""
Problem: Maximum Consecutive Ones

Given a binary array nums (containing only 0s and 1s), find the maximum number of 
consecutive 1s in the array.
"""

class MCO:
    def maximum_ones(self,nums):
        if(len(nums)<=1):
            return -1
        max_count=0
        count=0
        
        for val in nums:
            if(val==0):
                count=0
                continue
            else:
                count+=1  
                max_count=max(max_count,count)  
                # if(count>max_count):
                #     max_count=count
        return max_count
    
    
obj=MCO()
print(obj.maximum_ones([1, 1, 0, 0, 1, 1, 1, 0,0,0,0,0,1,1,1,1,1,1]))