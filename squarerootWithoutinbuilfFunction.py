class solution:
    def sqrt(self,num):
        if num<0:
            return None
        low,high=0 , num
        ans=0
        while(low<=high):
            mid=(low+high)//2
            
            if(mid*mid == num):
                return mid
            elif(mid*mid<num):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    
    

    
    
    
obj=solution()
print(obj.sqrt(16))