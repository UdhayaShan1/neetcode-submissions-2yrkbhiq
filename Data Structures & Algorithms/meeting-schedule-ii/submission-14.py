"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x.start)
        pq = []
        class Tmp:
            def __init__(self, s, e):
                self.s = s
                self.e = e
            def __lt__(self, o):
                return self.e < o.e
        
        days = 1
        for i in intervals:
            if len(pq) == 0:
                heapq.heappush(pq, Tmp(i.start, i.end))
            else:
                if i.start < pq[0].e:
                    days += 1
                else:
                    if pq and i.start >= pq[0].e:
                        heapq.heappop(pq)
                heapq.heappush(pq, Tmp(i.start, i.end))
        return days
        
