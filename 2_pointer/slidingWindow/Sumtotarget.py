
# Pair with Target Sum**
#    - Given a sorted array, find if there exists a pair of numbers that add up to a target sum.

# example1 = [1, 2, 3, 4, 6]
# target1 = 6


def pair_with_target_sum(arr, target_sum):
    i=0
    j=len(arr)-1
    sum=0
    while(i<j):
        sum=arr[i]+arr[j]
        if(sum==target_sum):
            return [arr[i],arr[j]]
        elif(sum > target_sum):
            j-=1
        else:
            i+=1
    
            
        
print(pair_with_target_sum([1, 2, 3, 4, 6],6))