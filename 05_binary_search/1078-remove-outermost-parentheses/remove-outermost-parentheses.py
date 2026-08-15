class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
                if count > 1:
                    result += '('
            elif ch == ')':
                count -= 1
                if count > 0:
                    result += ')'
        
        return result