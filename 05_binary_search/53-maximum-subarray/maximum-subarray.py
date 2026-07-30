class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_total = float('-inf')
        for i in range(0,len(nums)):
            total = total +nums[i]
            if total > max_total :
                max_total = total
            # drop total if it is -ve
            if total < 0:
                total =0
        return max_total