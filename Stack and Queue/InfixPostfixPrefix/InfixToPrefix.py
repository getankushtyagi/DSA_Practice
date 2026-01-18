# in this we need to once reverse the string and then perform infix to postfix and once you get the result again reverse 


class Solution:
    
    def precedence(self, s):
        
        if(s == "+" or s=="-"):
            return 1
        elif(s=="/" or s=="*"):
            return 2
        elif(s=="^"):
            return 3
        return 0
    
    def infixToPrefix(self,s):
        s=s[::-1]
        s=s.replace("(","temp").replace(")","(").replace("temp",")")
        
        stack=[]
        result=[]
        for val in s:
            if("a"<=val<='z' or "A"<=val<="Z" or "0"<=val<="9"):
                result.append(val)
            elif(val == "("):
                stack.append(val)
            elif(val == ")"):
                while(stack and stack[-1]=="("):
                    result.append(stack.pop())
                stack.pop()
            else:
                while(stack and self.precedence(stack[-1])>self.precedence(val)):
                    result.append(stack.pop())
                stack.append(val)
        while(stack):
            result.append(stack.pop())
        
        return "".join(result[::-1])
                
        
        
        
            
obj=Solution()
print(obj.infixToPrefix("a*(b+c)/d"))