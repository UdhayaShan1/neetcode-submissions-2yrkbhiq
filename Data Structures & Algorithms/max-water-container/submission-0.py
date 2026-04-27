class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        res = 0
        while i < j:
            gap = j-i
            res = max(res, min(heights[i], heights[j])*gap)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return res
