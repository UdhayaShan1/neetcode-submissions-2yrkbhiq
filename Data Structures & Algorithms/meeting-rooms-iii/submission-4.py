class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        class Room:
            def __init__(self, n):
                self.n = n
            def __lt__(self, o):
                return self.n < o.n
        rooms = []
        for i in range(n):
            heapq.heappush(rooms, Room(i))
        class Meeting:
            def __init__(self, s, e, room):
                self.s = s
                self.e = e
                self.r = room
            def __lt__(self, o):
                return self.e < o.e
        pq = []
        time = 0
        ref = {}
        for i in range(len(meetings)):
            print(meetings[i], i)
            time = max(time, meetings[i][0])
            while pq and time >= pq[0].e:
                curr = heapq.heappop(pq)
                heapq.heappush(rooms, Room(curr.r))
            if not rooms:
                time = pq[0].e
            while pq and time >= pq[0].e:
                curr = heapq.heappop(pq)
                heapq.heappush(rooms, Room(curr.r))
            
            r = heapq.heappop(rooms)
            gap = meetings[i][1]-meetings[i][0]
            print(r.n, meetings[i])
            ref[r.n] = ref.get(r.n, 0)+1
            heapq.heappush(pq, Meeting(time, time+gap, r.n))
        best = 0
        hi = -1
        for i in ref:
            if ref[i] > best:
                best = ref[i]
                hi = i
        return hi
        
        


