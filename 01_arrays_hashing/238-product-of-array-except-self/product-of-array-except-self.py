class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
# filling the pre multiplication
        res[0]=1
        for i in range(1,n):
            res[i]=nums[i-1]*res[i-1]

# filling the post multiplication 
        post=1
        for i in range(n-1,-1,-1):
            res[i]=res[i]*post
            post*=nums[i]
        return res
