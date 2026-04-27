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
        
        pq = []

        days = 0
        for i in intervals:
            if not pq:
                days += 1
                heapq.heappush(pq, Tmp(i.start, i.end))
            else:
                yes = False
                if pq and pq[0].e <= i.start:
                    yes = True
                    heapq.heappop(pq)
                if not yes:
                    days += 1
                heapq.heappush(pq, Tmp(i.start, i.end))
        return days
                

        