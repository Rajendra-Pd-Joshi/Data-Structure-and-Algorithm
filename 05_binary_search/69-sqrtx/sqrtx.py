class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1,x
        while l <= r :
            m = (l+r)//2
            # print(m)
            if m*m > x:
                r = m-1
            elif m*m < x:
                l = m+1
            else:
                return m
        return l-1