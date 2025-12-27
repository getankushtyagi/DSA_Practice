class PrimeNumber:
    def pn(self,num):
        if(num <=1):
            return "prime number"
        else:
            for i in range(2,num//2):
                if(num % i == 0):
                    return "not Prime"
            return "prime number"    
        
        
obj=PrimeNumber()
print(obj.pn(6))