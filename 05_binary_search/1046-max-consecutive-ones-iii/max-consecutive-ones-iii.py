class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=right=0
        maxlen = 0
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            if zeros <= k:
                maxlen = max(maxlen,right-left+1)
                right += 1
        return maxlen