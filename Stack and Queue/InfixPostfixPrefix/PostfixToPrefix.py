#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        stack=[]
        
        for val in post_exp:
            if val.isalnum():
                stack.append(val)
            else:
                op1=stack.pop()
                op2=stack.pop()
                
                newexp=f"{val}{op2}{op1}"
                stack.append(newexp)
        return stack[-1]