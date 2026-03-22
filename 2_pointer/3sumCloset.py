

"""
16. 3Sum Closest
Medium

Given an integer array nums of length n and an integer target, find three integers 
in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
"""


def threeSum(nums,target):
    nums=sorted(nums)
    result=[]
    if(len(nums)<3):
        return []
    # x=1
    # y=len(nums)-1
    for i in range(len(nums)-2):
        # # skip duplicates for i
        # if i > 0 and nums[i] == nums[i-1]:
        #     continue
                    
        x=i+1
        y=len(nums)-1
        diff=float('inf')
        result=[]
        while(x<y):
            d=abs((nums[x]+nums[y]+nums[i])-target)
            if diff>d:
                diff=d
                result=nums[x]+nums[y]+nums[i]
            if(nums[x]+nums[y]== -nums[i]):
                return [nums[i]+nums[x]+nums[y]]
            elif(nums[x]+nums[y]< -nums[i]):
                x+=1
            elif(nums[x]+nums[y]> -nums[i]):
                y-=1
                
    return result


# Test cases
if __name__ == "__main__":
    print("="*70)
    print("3SUM CLOSEST - TEST CASES")
    print("="*70)
    
    print("\nExample 1 from LeetCode:")
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    result1 = threeSum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Expected: 2 (because -1 + 2 + 1 = 2)")
    
    print("\nExample 2 from LeetCode:")
    nums2 = [0, 0, 0]
    target2 = 1
    result2 = threeSum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Expected: 0 (because 0 + 0 + 0 = 0)")
    
    print("\nTest Case 3: Target is achievable exactly")
    nums3 = [1, 1, 1, 0]
    target3 = 3
    result3 = threeSum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Expected: 3 (because 1 + 1 + 1 = 3)")
    
    print("\nTest Case 4: Negative numbers")
    nums4 = [-5, -3, -1, 0, 2, 4]
    target4 = -2
    result4 = threeSum(nums4, target4)
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {result4}")
    print(f"Expected: -2 (e.g., -5 + 0 + 4 = -1 or -5 + 2 + 0 = -3, closest is -2)")
    
    print("\nTest Case 5: All positive numbers")
    nums5 = [1, 2, 3, 4, 5]
    target5 = 10
    result5 = threeSum(nums5, target5)
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Output: {result5}")
    print(f"Expected: 9 (because 2 + 3 + 4 = 9)")
    
    print("\nTest Case 6: Large target")
    nums6 = [1, 2, 4, 8, 16, 32]
    target6 = 50
    result6 = threeSum(nums6, target6)
    print(f"Input: nums = {nums6}, target = {target6}")
    print(f"Output: {result6}")
    print(f"Expected: 52 (because 4 + 16 + 32 = 52)")
    
    print("\nTest Case 7: Minimum array size (3 elements)")
    nums7 = [1, 1, 1]
    target7 = 0
    result7 = threeSum(nums7, target7)
    print(f"Input: nums = {nums7}, target = {target7}")
    print(f"Output: {result7}")
    print(f"Expected: 3 (because 1 + 1 + 1 = 3)")
    
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
