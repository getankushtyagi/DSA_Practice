def palindrome(s):
    if(s==s[::-1]):
        return True
    else:
        return False


print(palindrome("ankush"))
print(palindrome("abc"))
print(palindrome("aba"))
print(palindrome("abba"))