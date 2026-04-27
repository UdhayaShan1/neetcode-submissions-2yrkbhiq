class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        heights.append(0)
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                pop = stack.pop()
                left = -1 if not stack else stack[-1]
                gap = i-left-1

                res = max(heights[pop]*gap, res)
            stack.append(i)
        return res