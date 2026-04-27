class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        initial = len(intervals)
        count = 1
        end = intervals[0][1]
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            ref = intervals[i]
            if ref[0] >= end:
                res.append(ref)
                end = ref[1]
        print(res)
        return initial-len(res)