# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Pattern: One-pass hash map storing complements as we scan
# Time: O(n)   Space: O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # value -> index
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i
        return []



