"""
Problem: Maximum Sum Subarray of Size K

Given an array of integers arr and an integer k, find the maximum sum of a subarray of size k.

Example 1:
Input: arr = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr[2] + arr[3] = 300 + 400 = 700

Example 2:
Input: arr = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: Subarray [4, 2, 10, 23] has the maximum sum = 39

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= k <= arr.length
- 0 <= arr[i] <= 10^6

Approach: Sliding Window
Time Complexity: O(n) where n is the length of array
Space Complexity: O(1)
"""

class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 

        low=0
        high=k-1
        maxi=float("-inf")
        sum=0
        for i in range(k):
            sum+=arr[i]
        while(high<len(arr)):
            maxi=max(maxi,sum)
            sum-=arr[low]
            low+=1
            high+=1
            if(high<len(arr)):
                sum+=arr[high]
        return maxi
          
            
        
# Test cases
obj = Solution()

# Test case 1: Basic example
print("Test 1:", obj.maxSubarraySum([100, 200, 300, 400], 2))  # Expected: 700

# Test case 2: Larger array with k=4
print("Test 2:", obj.maxSubarraySum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))  # Expected: 39

# Test case 3: k equals array length
print("Test 3:", obj.maxSubarraySum([1, 2, 3, 4, 5], 5))  # Expected: 15

# Test case 4: k = 1 (single elements)
print("Test 4:", obj.maxSubarraySum([5, 2, 9, 1, 5, 6], 1))  # Expected: 9

# Test case 5: Negative numbers
print("Test 5:", obj.maxSubarraySum([-1, -2, -3, -4], 2))  # Expected: -3

# Test case 6: Mixed positive and negative
print("Test 6:", obj.maxSubarraySum([2, -1, 5, -3, 4, 6], 3))  # Expected: 10

# Test case 7: All same elements
print("Test 7:", obj.maxSubarraySum([5, 5, 5, 5, 5], 3))  # Expected: 15

# Test case 8: Large window
print("Test 8:", obj.maxSubarraySum([10, 20, 30, 40, 50], 3))  # Expected: 120