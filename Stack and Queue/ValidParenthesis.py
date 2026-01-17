class Solution:
    def __init__(self):
        # Define Data Structures
        self.items=[]

    def isValid(self, s: str) -> bool:
        
        if(len(s)<=1):
            return False
        
        dict={
            "]": "[",
            ")": "(",
            "}": "{"
        }
        
        for val in s:
            if(val in ["[","{","("]):
                self.items.append(val)
            elif(val in ["}","]",")"]):
                if(self.items and self.items[-1] == dict[val]):
                    self.items.pop()
                else:
                    return False
        return len(self.items) == 0
        
obj=Solution()
print(obj.isValid("){"))