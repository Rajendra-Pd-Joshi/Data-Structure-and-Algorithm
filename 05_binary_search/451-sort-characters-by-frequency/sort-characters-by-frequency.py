class Solution:
    def frequencySort(self, s: str) -> str:
        mapping = {}

        for i in s:
            mapping[i] = mapping.get(i,0)+1

        result = sorted(mapping.items(),key=lambda x:-x[1])
        ans =''
        for key,value in result:
            ans = ans + key*value
        return ans
        