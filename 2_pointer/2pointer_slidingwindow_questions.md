
## 2 Pointer Questions (20 with Explanations & Examples)

1. **Pair with Target Sum**
   - **Description:** Given a sorted array, find if there exists a pair of numbers that add up to a target sum.
   - **Example 1:** nums = [1,2,3,4,6], target = 6 → Output: True (2+4)
   - **Example 2:** nums = [2,5,9,11], target = 11 → Output: True (2+9)

2. **Remove Duplicates from Sorted Array**
   - **Description:** Remove duplicates in-place so each unique element appears only once. Return the new length.
   - **Example 1:** nums = [1,1,2] → Output: 2, nums = [1,2,_]
   - **Example 2:** nums = [0,0,1,1,1,2,2,3,3,4] → Output: 5, nums = [0,1,2,3,4,_...]

3. **Move Zeroes**
   - **Description:** Move all zeroes to the end while maintaining the order of non-zero elements.
   - **Example 1:** nums = [0,1,0,3,12] → Output: [1,3,12,0,0]
   - **Example 2:** nums = [0,0,1] → Output: [1,0,0]

4. **Reverse a String**
   - **Description:** Reverse the characters of a string using two pointers.
   - **Example 1:** s = "ankush" → Output: "hskuna"
   - **Example 2:** s = "hello" → Output: "olleh"

5. **Container With Most Water**
   - **Description:** Given n non-negative integers representing heights, find two lines that together with the x-axis form a container, such that the container contains the most water.
   - **Example 1:** height = [1,8,6,2,5,4,8,3,7] → Output: 49
   - **Example 2:** height = [1,1] → Output: 1

6. **Valid Palindrome**
   - **Description:** Check if a string is a palindrome, considering only alphanumeric characters and ignoring cases.
   - **Example 1:** s = "A man, a plan, a canal: Panama" → Output: True
   - **Example 2:** s = "race a car" → Output: False

7. **Merge Two Sorted Arrays**
   - **Description:** Merge two sorted arrays into one sorted array in-place.
   - **Example 1:** nums1 = [1,2,3,0,0,0], nums2 = [2,5,6] → Output: [1,2,2,3,5,6]
   - **Example 2:** nums1 = [1], nums2 = [] → Output: [1]

8. **Remove Element**
   - **Description:** Remove all instances of a value in-place and return the new length.
   - **Example 1:** nums = [3,2,2,3], val = 3 → Output: 2, nums = [2,2,_]
   - **Example 2:** nums = [0,1,2,2,3,0,4,2], val = 2 → Output: 5, nums = [0,1,3,0,4,_...]

9. **Squares of a Sorted Array**
   - **Description:** Return an array of the squares of each number sorted in non-decreasing order.
   - **Example 1:** nums = [-4,-1,0,3,10] → Output: [0,1,9,16,100]
   - **Example 2:** nums = [-7,-3,2,3,11] → Output: [4,9,9,49,121]

10. **Subarray with Given Sum**
   - **Description:** Find a continuous subarray that adds up to a given sum.
   - **Example 1:** arr = [1,2,3,7,5], sum = 12 → Output: [2,3,7]
   - **Example 2:** arr = [1,4,20,3,10,5], sum = 33 → Output: [20,3,10]

11. **Find the Duplicate Number**
   - **Description:** Given an array with n+1 integers where each integer is between 1 and n, find the duplicate number.
   - **Example 1:** nums = [1,3,4,2,2] → Output: 2
   - **Example 2:** nums = [3,1,3,4,2] → Output: 3

12. **Intersection of Two Arrays II**
   - **Description:** Find the intersection of two arrays, including duplicates.
   - **Example 1:** nums1 = [1,2,2,1], nums2 = [2,2] → Output: [2,2]
   - **Example 2:** nums1 = [4,9,5], nums2 = [9,4,9,8,4] → Output: [4,9]

13. **Backspace String Compare**
   - **Description:** Given two strings, return if they are equal when both are typed into empty text editors. '#' means a backspace character.
   - **Example 1:** S = "ab#c", T = "ad#c" → Output: True
   - **Example 2:** S = "a##c", T = "#a#c" → Output: True

14. **Minimum Size Subarray Sum**
   - **Description:** Find the minimal length of a contiguous subarray of which the sum ≥ s.
   - **Example 1:** s = 7, nums = [2,3,1,2,4,3] → Output: 2 ([4,3])
   - **Example 2:** s = 4, nums = [1,4,4] → Output: 1 ([4])

15. **Sort Colors (Dutch National Flag Problem)**
   - **Description:** Sort an array with 0s, 1s, and 2s in-place.
   - **Example 1:** nums = [2,0,2,1,1,0] → Output: [0,0,1,1,2,2]
   - **Example 2:** nums = [2,0,1] → Output: [0,1,2]

16. **Find All Anagrams in a String**
   - **Description:** Find all start indices of p's anagrams in s.
   - **Example 1:** s = "cbaebabacd", p = "abc" → Output: [0,6]
   - **Example 2:** s = "abab", p = "ab" → Output: [0,1,2]

17. **Longest Mountain in Array**
   - **Description:** Return the length of the longest mountain.
   - **Example 1:** arr = [2,1,4,7,3,2,5] → Output: 5 ([1,4,7,3,2])
   - **Example 2:** arr = [2,2,2] → Output: 0

18. **Find the Longest Substring with At Most Two Distinct Characters**
   - **Description:** Given a string, find the length of the longest substring with at most two distinct characters.
   - **Example 1:** s = "eceba" → Output: 3 ("ece")
   - **Example 2:** s = "ccaabbb" → Output: 5 ("aabbb")

19. **Find the Longest Subarray with Sum Less Than K**
   - **Description:** Find the longest subarray with sum less than k.
   - **Example 1:** arr = [1,2,1,0,1], k = 4 → Output: 4 ([1,2,1,0])
   - **Example 2:** arr = [1,2,3,4], k = 5 → Output: 2 ([1,2])

20. **Find the Pair with the Closest Sum to X**
   - **Description:** Given a sorted array and a number X, find the pair whose sum is closest to X.
   - **Example 1:** arr = [10,22,28,29,30,40], X = 54 → Output: (22, 30)
   - **Example 2:** arr = [1,3,4,7,10], X = 15 → Output: (4,10)

---

## Sliding Window Questions (20 with Explanations & Examples)

1. **Maximum Sum Subarray of Size K**
   - **Description:** Find the maximum sum of any contiguous subarray of size k.
   - **Example 1:** arr = [2,1,5,1,3,2], k = 3 → Output: 9 ([5,1,3])
   - **Example 2:** arr = [2,3,4,1,5], k = 2 → Output: 7 ([3,4])

2. **Smallest Subarray with a Greater Sum**
   - **Description:** Find the length of the smallest contiguous subarray whose sum is greater than or equal to S.
   - **Example 1:** arr = [2,1,5,2,3,2], S = 7 → Output: 2 ([5,2])
   - **Example 2:** arr = [2,1,5,2,8], S = 7 → Output: 1 ([8])

3. **Longest Substring with K Distinct Characters**
   - **Description:** Find the length of the longest substring with no more than K distinct characters.
   - **Example 1:** s = "araaci", K = 2 → Output: 4 ("araa")
   - **Example 2:** s = "cbbebi", K = 3 → Output: 5 ("cbbeb" or "bbebi")

4. **Longest Substring Without Repeating Characters**
   - **Description:** Find the length of the longest substring without repeating characters.
   - **Example 1:** s = "abcabcbb" → Output: 3 ("abc")
   - **Example 2:** s = "bbbbb" → Output: 1 ("b")

5. **Fruits into Baskets**
   - **Description:** Find the length of the longest subarray with at most two distinct characters.
   - **Example 1:** fruits = [1,2,1] → Output: 3
   - **Example 2:** fruits = [0,1,2,2] → Output: 3

6. **Longest Subarray with Ones after Replacement**
   - **Description:** Find the length of the longest subarray with 1s after replacing at most K 0s with 1s.
   - **Example 1:** arr = [0,1,1,0,0,1,1,0], K = 2 → Output: 6
   - **Example 2:** arr = [1,1,0,0,1,1,1,0,1], K = 2 → Output: 7

7. **Permutation in String**
   - **Description:** Check if s2 contains a permutation of s1.
   - **Example 1:** s1 = "ab", s2 = "eidbaooo" → Output: True
   - **Example 2:** s1 = "ab", s2 = "eidboaoo" → Output: False

8. **Minimum Window Substring**
   - **Description:** Find the minimum window in s which will contain all the characters in t.
   - **Example 1:** s = "ADOBECODEBANC", t = "ABC" → Output: "BANC"
   - **Example 2:** s = "a", t = "a" → Output: "a"

9. **Longest Substring with At Most Two Distinct Characters**
   - **Description:** Find the length of the longest substring with at most two distinct characters.
   - **Example 1:** s = "eceba" → Output: 3 ("ece")
   - **Example 2:** s = "ccaabbb" → Output: 5 ("aabbb")

10. **Count Occurrences of Anagrams**
   - **Description:** Count all anagrams of a pattern in a string.
   - **Example 1:** txt = "forxxorfxdofr", pat = "for" → Output: 3
   - **Example 2:** txt = "aabaabaa", pat = "aaba" → Output: 4

11. **Longest Substring with All Vowels Present**
   - **Description:** Find the length of the longest substring containing all vowels at least once.
   - **Example 1:** s = "aeiouu" → Output: 5
   - **Example 2:** s = "aeeeiiiioooauuuaeiou" → Output: 10

12. **Longest Substring with At Most K Repeating Characters**
   - **Description:** Find the length of the longest substring with at most K repeating characters.
   - **Example 1:** s = "aaabbcc", K = 2 → Output: 4 ("aabb" or "bbcc")
   - **Example 2:** s = "aabacbebebe", K = 3 → Output: 7 ("cbebebe")

13. **Maximum Number of Vowels in a Substring of Given Length**
   - **Description:** Find the maximum number of vowels in any substring of length k.
   - **Example 1:** s = "abciiidef", k = 3 → Output: 3
   - **Example 2:** s = "aeiou", k = 2 → Output: 2

14. **Longest Substring with Same Letters after Replacement**
   - **Description:** Find the length of the longest substring containing the same letter after replacing at most K other letters.
   - **Example 1:** s = "ABAB", K = 2 → Output: 4
   - **Example 2:** s = "AABABBA", K = 1 → Output: 4

15. **Maximum Average Subarray I**
   - **Description:** Find the contiguous subarray of length k that has the maximum average value.
   - **Example 1:** nums = [1,12,-5,-6,50,3], k = 4 → Output: 12.75
   - **Example 2:** nums = [5], k = 1 → Output: 5.0

16. **Number of Subarrays of Size K and Average Greater than or Equal to Threshold**
   - **Description:** Count the number of subarrays of size k with average ≥ threshold.
   - **Example 1:** arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4 → Output: 3
   - **Example 2:** arr = [1,1,1,1,1], k = 1, threshold = 0 → Output: 5

17. **Longest Substring with At Most K Distinct Characters**
   - **Description:** Find the length of the longest substring with at most K distinct characters.
   - **Example 1:** s = "eceba", K = 2 → Output: 3
   - **Example 2:** s = "aa", K = 1 → Output: 2

18. **Sliding Window Maximum**
   - **Description:** Find the maximum value in each sliding window of size k.
   - **Example 1:** nums = [1,3,-1,-3,5,3,6,7], k = 3 → Output: [3,3,5,5,6,7]
   - **Example 2:** nums = [1], k = 1 → Output: [1]

19. **Longest Substring with At Most K Unique Characters**
   - **Description:** Find the length of the longest substring with at most K unique characters.
   - **Example 1:** s = "aabacbebebe", K = 3 → Output: 7
   - **Example 2:** s = "aaaa", K = 1 → Output: 4

20. **Count Number of Nice Subarrays**
   - **Description:** Count the number of subarrays with exactly k odd numbers.
   - **Example 1:** nums = [1,1,2,1,1], k = 3 → Output: 2
   - **Example 2:** nums = [2,4,6], k = 1 → Output: 0

---

Happy Coding!
