class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ')' or c == ']' or c == '}':
                if not stack:
                    return False
                if c == ')' and stack[-1] != '(':
                    return False
                if c == ']' and stack[-1] != '[':
                    return False
                if c == '}' and stack[-1] != '{':
                    return False
                
                stack.pop()

            else:
                stack.append(c)
            
        return True if not stack else False