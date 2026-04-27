class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max1 = -float('inf')
        res = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max1:
                res.append(i)
            max1 = max(max1, heights[i])
        return res[::-1]
