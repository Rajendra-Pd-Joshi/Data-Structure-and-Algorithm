class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(i,j,target):
            l=j+1
            r=len(nums)-1
            while l<r:
                sum= nums[l]+nums[r]
                if sum < target:
                    l +=1
                elif sum > target:
                    r-=1
                else:
                    res.append([nums[i],nums[j],nums[l],nums[r]])
                    while l<len(nums)-1 and nums[l]== nums[l+1]:
                        l+=1
                    while r>0 and nums[r] == nums[r-1]:
                        r-=1
                    
                    l+=1
                    r-=1
        
        
        nums.sort()
        res=[]
        
        for i in range(len(nums)-3):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue

                subTarget=target-nums[i]-nums[j]

                twoSum(i,j,subTarget)
        return res

        