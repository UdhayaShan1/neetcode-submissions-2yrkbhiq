class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        class Rooms:
            def __init__(self, no):
                self.n = no
            
            def __lt__(self, o):
                return self.n < o.n
        
        class Meeting:
            def __init__(self, s, e, room=-1):
                self.s = s
                self.e = e
                self.room = room
            def __lt__(self, o):
                return self.e < o.e
        

        r = []
        m = []
        count = {}
        for i in range(n):
            count[i] = 0
            heapq.heappush(r, Rooms(i))
        meetings.sort(key=lambda x:x[0])
        time = 0
        for i in meetings:
            if r:
                while m and m[0].e <= max(time, i[0]):
                    heapq.heappush(r, Rooms(heapq.heappop(m).room))
                room = heapq.heappop(r)
                count[room.n] += 1
                duration = i[1]-i[0]
                heapq.heappush(m, Meeting(max(time, i[0]), max(time, i[0])+duration, room.n))
            else:
                time = m[0].e
                while m and m[0].e <= time:
                    heapq.heappush(r, Rooms(heapq.heappop(m).room))
                room = heapq.heappop(r)
                count[room.n] += 1
                duration = i[1]-i[0]
                heapq.heappush(m, Meeting(max(time, i[0]), max(time, i[0])+duration, room.n))
        #print(count)

        most = max(count.values())
        res = float('inf')
        for i in count:
            if count[i] == most:
                res = min(res, i)
        return res
                

