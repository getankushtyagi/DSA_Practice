"""given an array arr of positive integers and an integer x. Return the frequency of x in the array.

Examples :

Input: arr = [1, 1, 1, 1, 1], x = 1
Output: 5
Explanation: Frequency of 1 is 5.
"""
arr = [1, 1, 1, 1, 1]

hash_dict={}

for x in arr:
    if x in hash_dict:
        hash_dict[x]+=1
    else:
        hash_dict[x]=1
        
# print hash_dict
print(hash_dict)
# answer
print(hash_dict[1])