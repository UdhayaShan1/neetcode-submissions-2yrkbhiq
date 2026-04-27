class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = 0
        end = len(intervals)-1
        res = float('inf')
        while start <= end:
            mid = (start+end)//2
            if intervals[mid][0] >= newInterval[0]:
                res = min(res, mid)
                end = mid-1
            else:
                start = mid+1
        #print(res)
        if res == float('inf'):
            intervals = intervals+[newInterval]
        elif res == 0:
            intervals = [newInterval]+intervals

        stack = []
        for i in range(len(intervals)):
            if i == res:
                stack.append(newInterval)
            while len(stack) > 1 and stack[-2][1] >= stack[-1][0]:
                ref = [stack[-2][0], max(stack[-2][1], stack[-1][1])]
                stack.pop()
                stack.pop()
                stack.append(ref)

            stack.append(intervals[i])

            while len(stack) > 1 and stack[-2][1] >= stack[-1][0]:
                ref = [stack[-2][0], max(stack[-2][1], stack[-1][1])]
                stack.pop()
                stack.pop()
                stack.append(ref)
        return stack

