"""
Problem: Convert Prefix Expression to Postfix

Given a prefix expression, convert it to postfix notation.
Prefix: operators come before operands (+AB)
Postfix: operators come after operands (AB+)
Process from right to left and use a stack.
Example: "*+ABC" -> "AB+C*"
"""

#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        stack=[]
        
        for val in pre_exp[::-1]:
            if val.isalnum():
                stack.append(val)
            else:
                op1=stack.pop()
                op2=stack.pop()
                
                new_exp=f"{op1}{op2}{val}"
                stack.append(new_exp)
                
        return stack[-1]