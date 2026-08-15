class Solution:
    def romanToInt(self, s: str) -> int:
        mapping ={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        n = len(s)
        for i in range(0,n):
            if i<n-1 and mapping[s[i]] < mapping[s[i+1]]:
                result -= mapping[s[i]]
            else:
                result += mapping[s[i]]
        
        return result