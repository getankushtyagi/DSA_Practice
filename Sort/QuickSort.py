class Quick:
    def quick_sort(self,arr):
        
        if(len(arr)<=1):
            return arr
        
        pivot=arr[len(arr)//2]
        left= [x for x in arr if x<pivot]
        middle=[x for x in arr if x==pivot]
        right=[x for x in arr if x>pivot]
        
        return self.quick_sort(left) + middle + self.quick_sort(right)



quick=Quick()
print(quick.quick_sort([64, 34, 25, 12, 22, 11, 90]))        