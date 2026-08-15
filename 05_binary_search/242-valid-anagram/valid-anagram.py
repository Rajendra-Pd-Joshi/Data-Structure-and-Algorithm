class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping ={}

        for i in s:
            mapping[i] = mapping.get(i,0)+1
        for i in t:
            mapping[i] = mapping.get(i,0)-1
        
        for i in mapping:
            if mapping[i]!=0:
                return False
        return True