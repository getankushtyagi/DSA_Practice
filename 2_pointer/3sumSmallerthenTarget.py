

"""
Given an array arr[] of distinct integers of size n and a value sum, the task is to find the count of triplets (i, j, k),
having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.

Examples :

Input: n = 4, sum = 2, arr[] = {-2, 0, 1, 3}
Output:  2
Explanation: Below are triplets with sum less than 2 (-2, 0, 1) and (-2, 0, 3). 
Input: n = 5, sum = 12, arr[] = {5, 1, 3, 4, 7}
Output: 4
Explanation: Below are triplets with sum less than 12 (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).
"""

# we need to check the test cases

def threeSum(nums, target):
    nums.sort()
    count = 0
    
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < target:
                # key insight:
                # all elements from left → right-1 will also work
                count += (right - left)
                left += 1
            else:
                right -= 1
                
    return count

# Test cases
if __name__ == "__main__":
    print("="*70)
    print("3SUM SMALLER THAN TARGET - TEST CASES")
    print("="*70)
    
    print("\nExample 1 from Problem:")
    nums1 = [-2, 0, 1, 3]
    target1 = 2
    result1 = threeSum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print(f"Explanation: Triplets with sum < 2 are: (-2, 0, 1) and (-2, 0, 3)")
    
    print("\nExample 2 from Problem:")
    nums2 = [5, 1, 3, 4, 7]
    target2 = 12
    result2 = threeSum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Expected: 4")
    print(f"Explanation: Triplets are: (1, 3, 4), (1, 3, 5), (1, 3, 7), (1, 4, 5)")
    
    print("\nTest Case 3: No triplets smaller than target")
    nums3 = [3, 5, 7]
    target3 = 10
    result3 = threeSum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Expected: 0")
    print(f"Explanation: 3 + 5 + 7 = 15, which is >= 10")
    
    print("\nTest Case 4: All triplets smaller than target")
    nums4 = [1, 1, 1, 1]
    target4 = 10
    result4 = threeSum(nums4, target4)
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {result4}")
    print(f"Expected: 4")
    print(f"Explanation: All combinations of 3 elements sum to 3, which is < 10")
    
    print("\nTest Case 5: Negative numbers")
    nums5 = [-5, -3, -1, 0, 2]
    target5 = 0
    result5 = threeSum(nums5, target5)
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Output: {result5}")
    print(f"Expected: Count of triplets with sum < 0")
    
    print("\nTest Case 6: Mixed positive and negative")
    nums6 = [-2, -1, 0, 1, 2, 3]
    target6 = 2
    result6 = threeSum(nums6, target6)
    print(f"Input: nums = {nums6}, target = {target6}")
    print(f"Output: {result6}")
    print(f"Expected: Count of triplets with sum < 2")
    
    print("\nTest Case 7: Three elements exactly")
    nums7 = [1, 2, 3]
    target7 = 7
    result7 = threeSum(nums7, target7)
    print(f"Input: nums = {nums7}, target = {target7}")
    print(f"Output: {result7}")
    print(f"Expected: 1")
    print(f"Explanation: (1, 2, 3) sum = 6 < 7")
    
    print("\nTest Case 8: Three elements, no valid triplets")
    nums8 = [1, 2, 3]
    target8 = 5
    result8 = threeSum(nums8, target8)
    print(f"Input: nums = {nums8}, target = {target8}")
    print(f"Output: {result8}")
    print(f"Expected: 0")
    print(f"Explanation: (1, 2, 3) sum = 6 >= 5")
    
    print("\nTest Case 9: Large numbers")
    nums9 = [10, 20, 30, 40, 50]
    target9 = 100
    result9 = threeSum(nums9, target9)
    print(f"Input: nums = {nums9}, target = {target9}")
    print(f"Output: {result9}")
    print(f"Expected: Count of triplets with sum < 100")
    
    print("\nTest Case 10: All negative")
    nums10 = [-10, -8, -6, -4, -2]
    target10 = -15
    result10 = threeSum(nums10, target10)
    print(f"Input: nums = {nums10}, target = {target10}")
    print(f"Output: {result10}")
    print(f"Expected: Count of triplets with sum < -15")
    
    print("\n" + "="*70)
    print("✅ All test cases completed!")
    print("="*70)

    
    print("\nTest Case 8: Duplicates with different target")
    nums8 = [-1, 0, 1, 1, 55]
    target8 = 3
    result8 = threeSum(nums8, target8)
    print(f"Input: nums = {nums8}, target = {target8}")
    print(f"Output: {result8}")
    print(f"Expected: 2 (because -1 + 1 + 1 = 1 or 0 + 1 + 1 = 2)")
    
    print("\nTest Case 9: Mixed positive and negative")
    nums9 = [-10, -5, 0, 5, 10]
    target9 = 7
    result9 = threeSum(nums9, target9)
    print(f"Input: nums = {nums9}, target = {target9}")
    print(f"Output: {result9}")
    print(f"Expected: 5 (because -5 + 0 + 10 = 5)")
    
    print("\nTest Case 10: Large negative target")
    nums10 = [-100, -50, -25, -10, -5]
    target10 = -100
    result10 = threeSum(nums10, target10)
    print(f"Input: nums = {nums10}, target = {target10}")
    print(f"Output: {result10}")
    print(f"Expected: -85 (because -50 + -25 + -10 = -85)")
    
    print("\nTest Case 11: Original test")
    nums11 = [-1, 0, 1, 2, -1, 4]
    target11 = 0
    result11 = threeSum(nums11, target11)
    print(f"Input: nums = {nums11}, target = {target11}")
    print(f"Output: {result11}")
    print(f"Expected: Closest sum to 0")
    
    print("\nTest Case 12: Target much larger than possible sum")
    nums12 = [1, 2, 3]
    target12 = 100
    result12 = threeSum(nums12, target12)
    print(f"Input: nums = {nums12}, target = {target12}")
    print(f"Output: {result12}")
    print(f"Expected: 6 (because 1 + 2 + 3 = 6)")
    
    print("\n" + "="*70)
    print("✅ All test cases completed!")
    print("="*70)
