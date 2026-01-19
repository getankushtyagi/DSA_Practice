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
