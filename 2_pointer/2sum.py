# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order. 

# with the help of two pointers  if array is sorted


# this is not handle the duplicate value currently every thing is uniue
def twoPointer(nums, target):
    i=0
    j=len(nums)-1
    if i==j or len(nums)==1:
        return nums
        
    while i<=j:
        if nums[i]+nums[j] == target:
            return [i,j]
        elif nums[i]+nums[j]<target:
            i+=1
        else:
            j-=1
    return None


# handle if array has duplicate values      
def twoSumWithDuplicate(nums, target):
    
    i=0
    j=len(nums)-1
    if(i==j or len(nums)==1):
        return nums
    result=[]
    while(i<j):
        if(i<j and nums[i]+nums[j]==target):
            result.append([i,j])
            i+=1
            j-=1
        if(nums[i]+nums[j]<target):
            i+=1
            while(nums[i]==nums[i-1]):
                i+=1
        if(nums[i]+nums[j]>target):
            j-=1
            while(i<j and nums[j]==nums[j+1]):
                j-=1
    return result
            
        
    
            
# Test cases
if __name__ == "__main__":
    print("="*60)
    print("TWO SUM - TWO POINTER APPROACH TEST CASES")
    print("="*60)
    
    print("\nTest Case 1: Basic case")
    nums1 = [5, 25, 75]
    target1 = 100
    result1 = twoPointer(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Expected: [1, 2]")
    
    print("\nTest Case 2: Two elements at ends")
    nums2 = [2, 7, 11, 15]
    target2 = 17
    result2 = twoPointer(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Expected: [0, 3]")
    
    print("\nTest Case 3: Two elements at beginning")
    nums3 = [1, 2, 3, 4, 5]
    target3 = 3
    result3 = twoPointer(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Expected: [0, 1]")
    
    print("\nTest Case 4: Two elements in middle")
    nums4 = [1, 3, 5, 7, 9]
    target4 = 12
    result4 = twoPointer(nums4, target4)
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {result4}")
    print(f"Expected: [2, 3]")
    
    print("\nTest Case 5: Negative numbers")
    nums5 = [-5, -2, 0, 3, 8]
    target5 = 6
    result5 = twoPointer(nums5, target5)
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Output: {result5}")
    print(f"Expected: [1, 4]")
    
    print("\nTest Case 6: All negative numbers")
    nums6 = [-10, -5, -3, -1]
    target6 = -13
    result6 = twoPointer(nums6, target6)
    print(f"Input: nums = {nums6}, target = {target6}")
    print(f"Output: {result6}")
    print(f"Expected: [0, 2]")
    
    print("\nTest Case 7: With zeros")
    nums7 = [-2, 0, 1, 3, 5]
    target7 = 1
    result7 = twoPointer(nums7, target7)
    print(f"Input: nums = {nums7}, target = {target7}")
    print(f"Output: {result7}")
    print(f"Expected: [0, 3] or [1, 2]")
    
    print("\nTest Case 8: Large numbers")
    nums8 = [100, 200, 300, 400, 500]
    target8 = 600
    result8 = twoPointer(nums8, target8)
    print(f"Input: nums = {nums8}, target = {target8}")
    print(f"Output: {result8}")
    print(f"Expected: [1, 3]")
    
    print("\nTest Case 9: Two elements only")
    nums9 = [3, 5]
    target9 = 8
    result9 = twoPointer(nums9, target9)
    print(f"Input: nums = {nums9}, target = {target9}")
    print(f"Output: {result9}")
    print(f"Expected: [0, 1]")
    
    print("\nTest Case 10: No solution exists")
    nums10 = [1, 2, 3, 4]
    target10 = 10
    result10 = twoPointer(nums10, target10)
    print(f"Input: nums = {nums10}, target = {target10}")
    print(f"Output: {result10}")
    print(f"Expected: None")
    
    print("\nTest Case 11: Duplicate numbers")
    nums11 = [1, 2, 3, 3, 4, 5]
    target11 = 6
    result11 = twoPointer(nums11, target11)
    print(f"Input: nums = {nums11}, target = {target11}")
    print(f"Output: {result11}")
    print(f"Expected: [1, 4] or [2, 3]")
    
    print("\nTest Case 12: Same number twice (if not same index)")
    nums12 = [2, 3, 4, 5, 6]
    target12 = 7
    result12 = twoPointer(nums12, target12)
    print(f"Input: nums = {nums12}, target = {target12}")
    print(f"Output: {result12}")
    print(f"Expected: [0, 4] or [1, 3]")
    
    print("\nTest Case 11: Duplicate numbers")
    nums11 = [1, 2, 3, 3, 4, 5]
    target11 = 6
    result12 = twoSumWithDuplicate(nums11, target11)
    print(f"Input: nums = {nums11}, target = {target11}")
    print(f"Output: {result12}")
    print(f"Expected: [1, 4] or [2, 3]")

    
    print("\n" + "="*60)
    print("✅ All test cases completed!")
    print("="*60)



