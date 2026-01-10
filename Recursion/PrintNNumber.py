# print descending order

def recursion(number):
    
    if(number):
        print(number)
        recursion(number-1)
        

recursion(10)