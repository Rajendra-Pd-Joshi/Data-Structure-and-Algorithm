class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        L = []
        L.extend(nums)
        L.extend(nums)
        return L