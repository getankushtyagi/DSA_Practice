

# Valid Palindrome**
#    - **Description:** Check if a string is a palindrome, considering only alphanumeric characters and ignoring cases.
#    - **Example 1:** s = "A man, a plan, a canal: Panama" → Output: True
#    - **Example 2:** s = "race a car" → Output: False



def isPalindrome(s: str) -> bool:
    s = s.replace(" ", "").replace(",", "").replace(".", "").replace(":","")
    s=s.lower()
    i=0
    j=len(s)-1
    while(i<=j):
        if(s[i]==s[j]):

            i+=1
            j-=1
            continue
        else:
            return False
    return True

        
    
#optimize version
    
def isPalindromeOptimize(s: str) -> bool:
    i, j = 0, len(s) - 1

    while i < j:
        # skip non-alphanumeric
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        # compare lowercase
        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True
    
    
    
    
print(isPalindrome("hi this is Ankush tyyagi"))
print(isPalindrome("A man, a plan, a canal: Panama"))



print(isPalindromeOptimize("hi this is Ankush tyyagi"))
print(isPalindromeOptimize("A man, a plan, a canal: Panama"))
