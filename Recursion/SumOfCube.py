class Solution:
    def sumOfSeries(self,n):
        #code here
        if(n<=1):
            return 1
        return n**3 + self.sumOfSeries(n-1)
obj=Solution()
print(obj.sumOfSeries(5))