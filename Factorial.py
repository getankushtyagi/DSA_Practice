class Factorial:
    def factorial(self,n):
        if(n<=1):
            return 1
        else:
            return n*self.factorial(n-1)
        
obj=Factorial()
print(obj.factorial(6))