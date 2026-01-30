class solution:
    def maxsubarraysum(self,arr):
        maximum=float("-inf")
        count=0
        for val in arr:
            maximum+=val
            
            count=max(maximum,count)
            
            if(maximum<0):
                maximum=0
        return count
            
            
obj=solution()

print(obj.maxsubarraysum( [2, 3, -8, 7, -1, 2, 3]))