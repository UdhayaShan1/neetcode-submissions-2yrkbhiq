class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        s = []
        for i in range(len(intervals)):
            s.append(intervals[i])
            while len(s) >= 2 and s[-2][1] >= s[-1][0]:
                last = s.pop()
                last1 = s.pop()
                s.append([min(last[0], last1[0]), max(last[-1], last1[-1])])
        return s
