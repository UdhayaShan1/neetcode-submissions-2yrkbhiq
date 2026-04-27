"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        class Min:
            def __init__(self, val):
                self.val = val
            def __lt__(self, o):
                return self.val < o.val
        intervals.sort(key=lambda x:x.start)
        if len(intervals) == 0:
            return 0
        ref = intervals[0]
        rooms = 1
        import heapq
        pq = []
        heapq.heappush(pq, Min(ref.end))

        
        for i in range(1, len(intervals)):
            chk = intervals[i]
            if chk.start >= pq[0].val:
                heapq.heappop(pq)
            else:
                rooms += 1
            heapq.heappush(pq, Min(chk.end))
        return rooms
        

