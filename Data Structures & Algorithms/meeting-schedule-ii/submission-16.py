"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        pq = []
        class Tmp:
            def __init__(self, s, e, room):
                self.s = s
                self.e = e
                self.r = room
            def __lt__(self, o):
                return self.e < o.e
        intervals.sort(key=lambda x:x.start)
        pq = []
        rooms = 1
        heapq.heappush(pq, Tmp(intervals[0].start, intervals[0].end, rooms))
        rooms_arr = []
        for i in range(1, len(intervals)):
            while pq and pq[0].e <= intervals[i].start:
                chk = heapq.heappop(pq)
                rooms_arr.append(chk.r)
            if not rooms_arr:
                rooms += 1
                heapq.heappush(pq, Tmp(intervals[i].start, intervals[i].end, rooms))
            else:
                heapq.heappush(pq, Tmp(intervals[i].start, intervals[i].end, rooms_arr.pop()))
        return rooms




