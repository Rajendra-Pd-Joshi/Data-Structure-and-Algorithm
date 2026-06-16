class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)-1
        i=0

        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
                i+=1
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
                # i+=1 you can't just increment i while swapping with right pointer
                
            else:
                i+=1