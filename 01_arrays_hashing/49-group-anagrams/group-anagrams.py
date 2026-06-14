class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            new_s = ''.join(sorted(s))
            result[new_s].append(s)
        return list(result.values())