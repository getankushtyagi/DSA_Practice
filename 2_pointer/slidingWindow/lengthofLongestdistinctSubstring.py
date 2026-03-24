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


# using sliding window approach, we can maintain a window that contains at most k distinct characters. We will expand the window by moving the high pointer and check the number of distinct characters in the current window. If it exceeds k, we will move the low pointer to shrink the window until we have at most k distinct characters again. We will keep track of the maximum length of valid substrings encountered during this process.

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

        return -1 if (maxi<k) else maxi

    # using hashmap to store the count of characters in the current window, we can efficiently check the number of distinct characters and update the maximum length of valid substrings.
    def longestKSubstrHash(self, s, k):
        low=0
        high=0
        key={}
        maxi=0
        while(high<len(s)):
            if s[high] in key:
                key[s[high]]+=1
            else:
                key[s[high]]=1
            count=len(key)
            if(count==k):
                maxi=max(maxi,(high-low+1))
                
            while(len(key)>k):
                key[s[low]]-=1
                if key[s[low]] == 0:
                    del key[s[low]]
                low+=1
            high+=1
        return -1 if (maxi<k) else maxi
            
        
        
obj = Solution()

print(obj.longestKSubstr("aabacbebebe", k=3))
print(obj.longestKSubstr("aaaa", k=2))
print(obj.longestKSubstr("aabaaab", k=2))   

print(obj.longestKSubstrHash("aabacbebebe", k=3))
print(obj.longestKSubstrHash("aaaa", k=2))
print(obj.longestKSubstrHash("aabaaab", k=2))   

