class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1

        Area=0
        while l<r :
            tempArea = min(height[l],height[r])*(r-l)
            Area= max(Area,tempArea)

            #  we have to maximize A=w* h 
            #  since w is decreasing so to get max A we have to go for max h

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return Area