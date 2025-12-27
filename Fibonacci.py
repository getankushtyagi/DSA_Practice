class Fibonacci:
    def fibonacci(self,n):
        if(n<=1):
            return n
        else:
            return self.fibonacci(n-1)+self.fibonacci(n-1)
        
        
obj=Fibonacci()
val=obj.fibonacci(9)
print(val)
            