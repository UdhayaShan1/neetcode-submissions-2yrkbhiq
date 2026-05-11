class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s = 0
        e = len(intervals)-1
        res = -1
        while s <= e:
            mid = (s+e)//2
            if intervals[mid][0] > newInterval[0]:
                e = mid-1
            else:
                
                s = mid+1
                res = s
        #print(res)
        if res == -1:
            intervals = [newInterval] + intervals
        else:
            intervals = intervals[:res] + [newInterval] + intervals[res:]
        #print(intervals)

        s = []
        for i in range(len(intervals)):
            s.append(intervals[i])
            while len(s) >= 2 and s[-2][1] >= s[-1][0]:
                last = s.pop()
                last1 = s.pop()
                s.append([min(last[0], last1[0]), max(last[-1], last1[-1])])
        return s

