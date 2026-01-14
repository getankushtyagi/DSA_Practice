"""
You are given an array arr[] containing positive integers.
The elements in the array arr[] range from  1 to n (where n is the size of the array),
and some numbers may be repeated or absent. Your have to count the frequency of all numbers in the range 1 to n 
and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).

Input: arr[] = [2, 3, 2, 3, 5]
Output: [0, 2, 2, 0, 1]
Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.

"""

class Solution:
    def frequencyCount(self, arr):
        #  code here
        
        hash_list=[0]*(len(arr)+1)
        for x in arr:
            hash_list[x]+=1
        
        
        for y in range(1,len(arr)):
            print(hash_list[y])
            
obj=Solution()
obj.frequencyCount([2, 3, 2, 3, 5])