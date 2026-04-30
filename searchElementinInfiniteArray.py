# Given a sorted array arr[] of infinite numbers. The task is to search for an element k in the array.

# Examples:

# Input: arr[] = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170], k = 10
# Output: 4
# Explanation: 10 is at index 4 in array.

# Input: arr[] = [2, 5, 7, 9], k = 3
# Output: -1
# Explanation: 3 is not present in array.


class sol:
    
    def binarySearch(self,arr, low, high, target):

        while low<=high:
            mid=(low+high)//2

            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1
                
                
    def findRange(self,arr,target):
        # first find the range in infinite array
        
        #we dont the len so start with first and second postion and compare with target 
        
        low=0
        high=1
        
        #here we short the array and creating a range like double the high and low according to the target in an indefinite array 
        while high < len(arr) and arr[high]<target:
            low=high
            high=high*2
        high = min(high,len(arr)-1)
        
        return self.binarySearch(arr,low,high,target)
    
    
    
obj=sol()

print(obj.findRange([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170], 10))