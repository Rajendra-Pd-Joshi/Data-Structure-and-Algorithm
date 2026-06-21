class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack = [] # pair -> (index,height)
        for i in range(len(heights)):
            idx = i
            while stack and stack[-1][1] > heights[i]:
                width = i-stack[-1][0]
                h = stack[-1][1]
                maxArea = max(maxArea,width*h)
                idx = stack[-1][0]
                stack.pop()
            stack.append((idx,heights[i]))
        
        while stack:
            width = len(heights)-stack[-1][0]
            h= stack[-1][1]
            maxArea = max(maxArea,width*h)
            stack.pop()
        return maxArea