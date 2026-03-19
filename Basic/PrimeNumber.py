"""
Problem: Prime Number Check

Determine if a given number is prime.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Example: 2, 3, 5, 7, 11, 13 are prime numbers.
"""

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