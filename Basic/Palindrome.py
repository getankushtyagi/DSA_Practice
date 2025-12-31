class Palindrom:
    def palindrome(self,val):
        
        rev_val=0
        while(val>0):
            rev_val=(rev_val*10)+val%10
            val=val//10
        print(rev_val)

pl=Palindrom()
pl.palindrome(121)