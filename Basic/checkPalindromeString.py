# without reucursion 
# def palindrome(s):
#     if(s==s[::-1]):
#         return True
#     else:
#         return False


    # not optimize for large string slicing fails when string is too large 
    
    # def palindrome( s):
    #     # base case
    #     if len(s) <= 1:
    #         return True
    
    #     # if first and last characters don't match
    #     if s[0] != s[-1]:
    #         return False
    
    #     # recursive call
    #     return isPalindrome(s[1:-1])
    
    
def palindrome( s):
    return check(s, 0, len(s) - 1)

def check( s, left, right):
        # base case
    if left >= right:
        return True

        # mismatch
    if s[left] != s[right]:
        return False

    # recursive call
    return check(s, left + 1, right - 1)



print(palindrome("ankush"))
print(palindrome("abc"))
print(palindrome("aba"))
print(palindrome("abba"))