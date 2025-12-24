class Sorting:
    def mergeSort(self,arr):
        if(len(arr)<2):
            return arr
        
        mid=len(arr)//2
        left=self.mergeSort(arr[:mid])
        right=self.mergeSort(arr[mid:])
        
        return self.merge(left,right)
    
    def merge(self,left,right):
        i=j=0
        result=[]
        
        while(i<len(left) and j<len(right)):
            if(left[i] <= right[j]):
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
sort=Sorting()
print(sort.mergeSort([64, 34, 25, 12, 22, 11, 90]))            
                
            
        
        
            
