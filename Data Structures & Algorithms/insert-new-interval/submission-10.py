class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #newInterval = [0, 0]
        start = 0
        end = len(intervals)-1
        res = -1
        while start <= end:
            mid = (start+end)//2
            if intervals[mid][0] <= newInterval[0]:
                res = max(res, mid)
                start = mid+1
            else:
                end = mid-1
        #print(res)
        if res == -1:
            arr = [newInterval]+intervals
        elif res == len(intervals)-1:
            arr = intervals+[newInterval]
        else:
            arr = []
            for i in range(len(intervals)):
                arr.append(intervals[i])
                if i == res:
                    arr.append(newInterval)
        #print(arr)

        stack = []
        for i in range(len(arr)):
            stack.append(arr[i])
            while len(stack) > 1 and stack[-2][1] >= stack[-1][0]:
                f = stack[-2]
                s = stack[-1]
                stack.pop()
                stack.pop()
                stack.append([f[0], max(f[1], s[1])])
        return stack
            
