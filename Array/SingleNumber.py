"""
Problem: Single Number

Given a non-empty array of integers where every element appears twice except for one, 
find that single element that appears only once.
Solution uses XOR bitwise operation for O(n) time and O(1) space complexity.
"""

# class SN:
#     def singleNumber(self,nums):
#         if(len(nums)<1):
#             return -1
#         elif(len(nums)==1):
#             return nums[0]
#         else:
#             for val in nums:
#                 count=0
#                 for val1 in nums:
#                     if(val==val1):
#                         count+=1
#                 if(count==1):
#                     return val
# obj=SN()
# print(obj.singleNumber([1, 2, 2, 4, 3, 1, 4]))


#optimize approach

class SN:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num #xor
        return result

obj = SN()
print(obj.singleNumber([1, 2, 2, 4, 3, 1, 4]))
