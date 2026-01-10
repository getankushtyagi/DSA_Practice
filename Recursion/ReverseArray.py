def reverse(arr,l,r):
    if(l>=r):
        return
    arr[l],arr[r]=arr[r],arr[l]
    reverse(arr,l+1,r-1)
    
arr=[1,2,3,4,5,6]
reverse(arr,0,len(arr)-1)
print(arr)    