class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # optimal solution
        result = [0]*len(nums)
        p = 0
        n = 1

        for i in nums:
            if i>=0:
                result[p]=i
                p+=2
            else:
                result[n]=i
                n+=2
        
        return result
        # time complexity is O(N+N)
        # space complexity is O(N)