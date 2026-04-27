class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = [-float('inf')]+heights+[-float('inf')]
        res = [0]*len(h)
        stack = []
        for i in range(len(h)):
            while stack and h[stack[-1]] > h[i]:
                res[stack[-1]] = i-stack[-1]-1
                stack.pop()
            stack.append(i)
        #print(res[1:-1])

        res2 = [0]*len(h)
        stack = []
        for i in range(len(h)):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            if stack:
                res2[i] = i-stack[-1]-1
            stack.append(i)
        #print(res2[1:-1])

        res = res[1:-1]
        res2 = res2[1:-1]

        r = 0
        for i in range(len(heights)):
            r = max(r, heights[i]*(res[i]+res2[i]+1))
        return r


