class SL:
    def second_largest(self,nums):
        
        if (len(nums)<=1):
            return -1 
        
        large=0
        second_large=0
        
        for x in nums:
            if(x > large):
                second_large=large
                large=x
            elif(x > second_large and x < large):
                second_large=x
        print(large,second_large)
        
sol=SL()
arr=[1,21,21,234,434,23234,453,21]
sol.second_largest(arr)
# print(sorted(arr))
print(set(arr))
        