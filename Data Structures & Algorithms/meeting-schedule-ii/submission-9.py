"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        class Tmp:
            def __init__(self, s, e):
                self.s = s
                self.e = e
            def __lt__(self, o):
                return self.e < o.e
        import heapq
        pq = []
        days = 0
        for i in range(len(intervals)):
            if pq and intervals[i].start >= pq[0].e:
                heapq.heappop(pq)
                heapq.heappush(pq, Tmp(intervals[i].start, intervals[i].end))
            else:
                days += 1
                heapq.heappush(pq, Tmp(intervals[i].start, intervals[i].end))
        return days