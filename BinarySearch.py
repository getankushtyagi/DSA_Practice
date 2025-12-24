class BS:
    def binary_search(self , nums, target):
        
        nums=self.quick_sort(nums)
        # nums = sorted(nums) inbuilt python function
        
        print("nums after sorting===", nums)
        
        low=0
        high=len(nums)-1
        
        while low <= high:
            middle=(low+high)//2
            if(nums[middle]==target):
                return middle
            elif(nums[middle]<target):
                low=middle+1
            else:
                high=middle-1
        return -1
                        
    
    def quick_sort(self, nums):
        if len(nums)<=1:
            return nums
        
        pivot=nums[len(nums)-1]
        left=[x for x in nums if x<pivot]
        middle=[x for x in nums if x==pivot]
        right=[x for x in nums if x>pivot]
        
        return self.quick_sort(left)+middle+self.quick_sort(right)
    
obj=BS()
print(obj.binary_search([23,43,56,32,232,1,324,545,65,64,2323,435,63434],2323))