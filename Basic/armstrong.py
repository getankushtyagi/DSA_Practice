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