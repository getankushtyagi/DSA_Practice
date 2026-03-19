"""
Problem: Print Numbers from N to 1 using Recursion

Given a number n, print all numbers from n down to 1 in descending order using recursion.
"""

# print descending order

def recursion(number):
    
    if(number):
        print(number)
        recursion(number-1)
        

recursion(10)