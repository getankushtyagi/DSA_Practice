class Solution:

    def precedence(self, s):
        if s in "+-":
            return 1
        elif s in "*/":
            return 2
        elif s == "^":
            return 3
        return 0
        
    def infixtoPostfix(self, s):
        result = []
        stack = []
        
        for val in s:
            if ("a" <= val <= "z") or ("A" <= val <= "Z") or ("0" <= val <= "9"):
                result.append(val)
            elif val == "(":
                stack.append(val)
            elif val == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while (
                        stack and
                        (
                            self.precedence(stack[-1]) > self.precedence(val) or
                            (self.precedence(stack[-1]) == self.precedence(val) and val != "^")
                        )
                    ):
                    result.append(stack.pop())
                stack.append(val)
                
        while stack:
            result.append(stack.pop())
                
        return "".join(result)
