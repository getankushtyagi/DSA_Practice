# here start from reverse only 
class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        stack=[]
        
        for val in pre_exp[::-1]:
            if val.isalnum():
                stack.append(val)
            else:
                op1=stack.pop()
                op2=stack.pop()
                
                new_val=f"({op1}{val}{op2})"
                stack.append(new_val)
        return stack[-1]