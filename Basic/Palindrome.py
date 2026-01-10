class Palindrom:
    # def palindrome(self,val):
        
    #     rev_val=0
    #     while(val>0):
    #         rev_val=(rev_val*10)+val%10
    #         val=val//10
    #     print(rev_val)
    
    @staticmethod
    def palindrome(s):
        s = str(s)  # Convert to string to handle both strings and numbers
        val=[True if s == s[::-1] else False]
        print(val)


pl=Palindrom()
pl.palindrome(121)
