class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapping1 = {}
        for i in range(len(s)):
            if s[i] in mapping:
               if mapping[s[i]] != t[i]:
                return False
            else:
                mapping[s[i]] = t[i]
            
            if t[i] in mapping1:
                if mapping1[t[i]] != s[i]:
                    return False
            else:
                mapping1[t[i]]= s[i]
        
        return True