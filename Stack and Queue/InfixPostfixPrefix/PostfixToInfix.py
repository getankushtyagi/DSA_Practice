"""
Problem: Convert Postfix Expression to Infix

Given a postfix expression (Reverse Polish Notation), convert it to infix notation.
Postfix: operators come after operands (AB+)
Infix: operators are between operands with parentheses ((A+B))
Use a stack to build the expression tree.
Example: "AB+C*" -> "((A+B)*C)"
"""

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