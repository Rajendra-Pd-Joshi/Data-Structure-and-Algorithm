class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # step 1: assuming
        count=0
        majority=None
        for i in nums:
            if count==0:
                majority=i
                count=1
            elif i==majority:
                count+=1
            else:
                count-=1

        # step 2: verification
        counter=0
        for i in nums:
            if i==majority:
                counter+=1
        if counter > len(nums)//2:
            return majority
        else:
            return None   
                
