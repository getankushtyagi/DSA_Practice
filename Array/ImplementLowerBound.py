class ILB:
    def lower_bound(self, nums, target):
        for x in nums:
            if x >= target:
                return x
        return -1  # target larger than all elements

obj=ILB()
print(obj.lower_bound([1,2,2,3,4,4,4,4,5,5,6,7,8,9,12],8))
            
                
            