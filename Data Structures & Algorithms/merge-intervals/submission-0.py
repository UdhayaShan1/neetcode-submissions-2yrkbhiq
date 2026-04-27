class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        stack = []
        for i in intervals:
            stack.append(i)
            while len(stack) > 1 and stack[-2][1] >= stack[-1][0]:
                f = stack[-2]
                s = stack[-1]
                stack.pop()
                stack.pop()
                stack.append([f[0], max(f[1], s[1])])
        return stack