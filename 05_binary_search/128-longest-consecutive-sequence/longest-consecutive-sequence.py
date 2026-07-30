class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        for i in nums:
            my_set.add(i)
        
        n = len(nums)
        largest = 0
        for num in my_set:
            if num-1 not in my_set:
                # means this is the starting point 
                x = num
                count = 1
                while x+1 in my_set:
                    count +=1
                    x +=1
                largest = max(largest,count)
        
        return largest