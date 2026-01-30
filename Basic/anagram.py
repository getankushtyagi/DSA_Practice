class solution:
    
    def anagram(self,s1,s2):
        if (len(s1)!=len(s2)):
            return False
        
        freq={}
        for val in s1:
            if val not in freq:
                freq[val]=1
            else:
                freq[val]+=1
    
        for el in s2:
            if el not in freq or freq[el]==0:
                return False
            else:
                freq[el]-=1
        return True
    
    
obj=solution()
print(obj.anagram("geeek","keeg"))