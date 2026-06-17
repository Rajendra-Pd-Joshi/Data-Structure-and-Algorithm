class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        n=len(height)
        left_max=[0]*n
        right_max=[0]*n

        i=1
        left_max[0]=height[0]
        while i<n:
            left_max[i]=max(height[i],left_max[i-1])
            i+=1
        
        i=n-2
        right_max[n-1]=height[n-1]
        while i>=0:
            right_max[i]=max(height[i],right_max[i+1])
            i-=1
        # print(height)
        # print(left_max)
        # print(right_max)

        for i in range(n):
            temp = min(left_max[i],right_max[i])-height[i]
            res += temp
        return res

