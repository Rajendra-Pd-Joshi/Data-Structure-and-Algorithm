class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # for the first majority element
        count1=0
        majority1=None
        
        # for the second majority element
        count2=0
        majority2=None

        # step 1: Assumption
        for i in nums:
            if majority1==i:
                count1+=1
            elif majority2==i:
                count2+=1
            elif count1==0:
                majority1=i
                count1=1
            elif count2==0:
                majority2=i
                count2=1
            else:
                count1-=1
                count2-=1
        
        # step 2:verification
        counter1=0
        counter2=0

        for i in nums:
            if i==majority1:
                counter1+=1
            if i==majority2:
                counter2+=1
            
        result=[]
        if counter1>len(nums)//3:
            result.append(majority1)
        if counter2>len(nums)//3:
            result.append(majority2)
        return result