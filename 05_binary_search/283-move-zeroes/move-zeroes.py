class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # edge case 1
        if len(nums)==1:
            return
        # find the first zero
        i=0
        while i<len(nums):
            if nums[i]==0:
                break
            i+=1
        
        # edge case 2
        if i == len(nums):
            return
        # find the non zero element after zero
        j = i+1
        
        while j<len(nums):
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            j+= 1
            
        
        