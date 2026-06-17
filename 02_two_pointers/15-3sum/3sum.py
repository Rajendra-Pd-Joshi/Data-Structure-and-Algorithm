class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def twoSum(l,target):
            r=len(nums)-1
            while l<r:
                sum= nums[l] + nums[r]
                if sum > target:
                    r-=1
                elif sum < target:
                    l+=1
                else:
                    res.append([-target,nums[l],nums[r]])
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    
                    l,r = l+1,r-1

        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            twoSum(i+1,-nums[i])
        return res