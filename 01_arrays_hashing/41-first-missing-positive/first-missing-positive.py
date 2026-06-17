class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # check for does it contains one or not
        containsOne = False
        # convert all <=0 and > len(nums) into 1
        for i in range(len(nums)):
            if nums[i]==1:
                containsOne=True
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        
        # check if one exist or not
        if containsOne==False:
            return 1

        for i in range(len(nums)):
            val=abs(nums[i])
            idx=val-1
            if nums[idx]<0:
                continue
            nums[idx]*=-1

        for i in range(len(nums)):
            if nums[i] >0:
                return i+1
        return len(nums)+1