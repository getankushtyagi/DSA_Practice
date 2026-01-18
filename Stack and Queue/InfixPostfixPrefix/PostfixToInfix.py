class Solution:
    
    def postfixtoinfix(self,s):
        
        stack=[]
        
        for val in s:
            if val.isalnum():
                stack.append(val)
            else:
                op1=stack.pop()
                op2=stack.pop()
                
                new_val=f"({op1}{val}{op2})"
                stack.append(new_val)
        return stack[-1]
    


obj=Solution()
print(obj.postfixtoinfix("ab*c+"))