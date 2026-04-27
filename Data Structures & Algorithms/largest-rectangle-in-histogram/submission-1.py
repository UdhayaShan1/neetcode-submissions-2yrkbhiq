class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hmm = heights + [-float('inf')]
        stack = []
        res = [0]*len(hmm)
        for i in range(len(hmm)):
            while stack and hmm[stack[-1]] > hmm[i]:
                res[stack[-1]] = i-stack[-1]-1
                stack.pop()
            stack.append(i)
        res = (res[:-1])

        hmm2 = [-float('inf')] + heights 
        stack = []
        res2 = [0]*len(hmm2)
        for i in range(len(hmm2)):
            while stack and hmm2[stack[-1]] >= hmm2[i]:
                stack.pop()
            if stack:
                res2[i] = i-stack[-1]-1
            stack.append(i)
        res2 = (res2[1:])

        hmm = 0
        for i in range(len(heights)):
            hmm = max(hmm, heights[i]*(1+res[i]+res2[i]))
        return hmm


