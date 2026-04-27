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
        import heapq
        pq = []
        for i in intervals:
            if len(pq) > 0 and i.start >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, i.end)
        return len(pq)