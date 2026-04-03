class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = [-float('inf')]+heights+[-float('inf')]
        s = []
        res = [0]*len(h)
        for i in range(len(h)):
            while s and h[s[-1]] > h[i]:
                res[s[-1]] = i-s[-1]-1
                s.pop()
            s.append(i)
        #print(res[1:])
        res = res[1:-1]

        res1 = [0]*len(h)
        for i in range(len(h)):
            while s and h[s[-1]] >= h[i]:
                s.pop()
            if s:
                res1[i] = i-s[-1]-1
            s.append(i)
        #print(res1[1:-1])
        res1 = res1[1:-1]

        r = -float('inf')
        for i in range(len(heights)):
            r = max(r, (1+res[i]+res1[i])*heights[i])
        return r

        