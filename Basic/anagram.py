'''
Check if two Strings are Anagrams of each other
Last Updated : 25 Jul, 2025
Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., if they contain the same characters with the same frequencies.

Examples:

Input: s1 = “geeks”  s2 = “kseeg”
Output: true
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Input: s1 = "allergy", s2 = "allergyy"
Output: false
'''


class solution:
    
    def anagram(self,s1,s2):
        if (len(s1)!=len(s2)):
            return False
        
        freq={}
        for val in s1:
            if val not in freq:
                freq[val]=1
            else:
                freq[val]+=1
    
        for el in s2:
            if el not in freq or freq[el]==0:
                return False
            else:
                freq[el]-=1
        return True
    
    
obj=solution()
print(obj.anagram("geeek","keeg"))