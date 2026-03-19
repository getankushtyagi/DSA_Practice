"""
Problem: Armstrong Number

Determine if a given number is an Armstrong number (also known as Narcissistic number).
An Armstrong number is a number that is equal to the sum of cubes of its digits.
Example: 153 is an Armstrong number because 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
"""

class AS:
    def armstrong(self, data):
        if(data <= 0):
            return data
        copy=data
        sum=0
        while(data):
            temp=data%10
            sum+=temp**3
            data=data//10
        if(copy==sum):
            return True
        else:
            return False
        
        
obj=AS()
print(obj.armstrong(153))