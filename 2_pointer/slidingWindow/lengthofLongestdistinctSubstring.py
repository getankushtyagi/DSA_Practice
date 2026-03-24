"""
You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

Note : If no such substring exists, return -1. 

Examples:

Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.
Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
"""



class Solution:
    def longestKSubstr(self, s, k):
        low = 0
        high = 0
        maxi = float("-inf")

        while high < len(s):
            str_sub = s[low:high+1]
            count = len(set(str_sub))

            if count == k:
                maxi = max(maxi, len(str_sub))

            while len(set(s[low:high+1])) > k:
                low += 1

            high += 1

        return maxi


obj = Solution()
print(obj.longestKSubstr("aabacbebebe", k=3))