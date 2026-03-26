# **Reverse a String**
#    - Reverse the characters of a string using the two pointer approach.


def reverse(s:str)->str:
    s=list(s)
    i=0
    j=len(s)-1
    
    while(i<j):
        s[i],s[j]= s[j],s[i]
        i+=1
        j-=1
        
    return "".join(s)


print(reverse("ankush"))