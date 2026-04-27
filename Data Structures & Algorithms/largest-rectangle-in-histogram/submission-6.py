class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [-float('inf')] + heights + [-float('inf')]
        res = [1]*len(heights)
        s = []
        for i in range(len(heights)):
            while s and heights[s[-1]] > heights[i]:
                res[s[-1]] = i-s[-1]
                s.pop()
            s.append(i)
        #res = res[1:-1]

        res2 = [1]*len(heights)
        s = []
        for i in range(len(heights)):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                res2[i] = i-s[-1]
            s.append(i)
        #res2 = res2[1:-1]
        print(res2)

        r = 0
        for i in range(1, len(heights)-1):
            width = res[i]+res2[i]-2+1
            r = max(r, heights[i]*width)
        return r
