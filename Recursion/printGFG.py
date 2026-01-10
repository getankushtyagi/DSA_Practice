class Solution:
    def printGfg(self, n):
        
        if(n==0):
            return
        print("GFG",end=" ")
        self.printGfg(n-1)
        
obj=Solution()
obj.printGfg(10)