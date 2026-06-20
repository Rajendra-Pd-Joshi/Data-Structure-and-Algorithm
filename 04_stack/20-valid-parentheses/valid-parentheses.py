class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch =='{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            else:
                if len(stack)==0 or ch != stack[-1]:
                    return False
                stack.pop()
            
        return True if len(stack)==0 else False