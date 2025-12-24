class MN:
    def missing_number(self,arr):
        if(len(arr)<=1):
            return -1
        
        for i in range(len(arr)):
            if(i==arr[i]):
                continue
            else:
                return i
sol=MN()
print(sol.missing_number([0,1,2,3,4,6]))