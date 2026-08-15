class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        ans = ''
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return ans
            ans += base[i]
        return ans