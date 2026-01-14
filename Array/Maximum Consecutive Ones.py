#brute force aaproach
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
                if(count>max_count):
                    max_count=count
        return max_count
    
    
obj=MCO()
print(obj.maximum_ones([1, 1, 0, 0, 1, 1, 1, 0,0,0,0,0,1,1,1,1,1,1]))