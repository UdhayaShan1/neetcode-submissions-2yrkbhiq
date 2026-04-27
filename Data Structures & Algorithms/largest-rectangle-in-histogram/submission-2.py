class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = [-float('inf')]+heights+[-float('inf')]
        res = [-1]*len(h)
        stack = []
        for i in range(len(h)):
            while stack and h[stack[-1]] > h[i]:
                res[stack[-1]] = i-stack[-1]-1
                stack.pop()
            stack.append(i)

        res = res[1:-1]


        res2 = [-1]*len(h)
        stack = []
        for i in range(len(h)):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            if stack:
                res2[i] = i-stack[-1]-1
            stack.append(i)
        res2 = res2[1:-1]
        #print(res,res2)

        r = -float('inf')
        for i in range(len(res)):
            r = max(r, heights[i]*(res[i]+res2[i]+1))
        return r



