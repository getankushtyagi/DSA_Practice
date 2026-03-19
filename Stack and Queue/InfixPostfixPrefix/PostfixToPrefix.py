"""
Problem: Convert Postfix Expression to Prefix

Given a postfix expression, convert it to prefix notation.
Postfix: operators come after operands (AB+)
Prefix: operators come before operands (+AB)
Use a stack to process operands and operators.
Example: "AB+C*" -> "*+ABC"
"""

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