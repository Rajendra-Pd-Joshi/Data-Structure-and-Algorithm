from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping = defaultdict(int)

        for i in s:
            mapping[i] += 1
        
        for i in t:
            mapping[i] -= 1

        for key,value in mapping.items():
            if value != 0:
                return False
        
        return True