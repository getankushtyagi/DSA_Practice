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
            
            
        