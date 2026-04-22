class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        h = len(heights)
        heights = heights+[float('inf')]
        s = []
        res = [-1]*len(heights)
        for i in range(len(heights)):
            while s and heights[s[-1]] <= heights[i]:
                res[s[-1]] = i-s[-1]
                s.pop()
            s.append(i)
        #print(res)

        r = []
        for i in range(len(heights)-1):
            if h-i == res[i]:
                r.append(i)
        return r

