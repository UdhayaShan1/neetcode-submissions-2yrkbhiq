class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = heights+[-float('inf')]
        s = []
        res = [0]*len(h)
        for i in range(len(h)):
            while s and h[i] < h[s[-1]]:
                res[s[-1]] = i-s[-1]-1
                s.pop()
            s.append(i)
        res = res[:-1]
        print(res)

        h = [-float('inf')]+heights
        s = []
        res1 = [0]*len(h)
        for i in range(len(h)):
            while s and h[i] <= h[s[-1]]:
                s.pop()
            if s:
                res1[i] = i-s[-1]-1
            s.append(i)
        print(res1[1:])
        res1 = res1[1:]
        r = 0
        for i in range(len(heights)):
            print(i, heights[i]*(1+res[i]+res1[i]))
            r = max(r, heights[i]*(1+res[i]+res1[i]))
        return r


