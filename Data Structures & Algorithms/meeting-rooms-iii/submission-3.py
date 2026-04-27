class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        class Rooms:
            def __init__(self, n):
                self.n = n
            def __lt__(self, o):
                return self.n < o.n
        class Wait:
            def __init__(self, s, e):
                self.s = s
                self.e = e
            def __lt__(self, o):
                return self.s < o.s
        
        class Taken:
            def __init__(self, s, e, r):
                self.s = s
                self.e = e
                self.r = r
            def __lt__(self, o):
                return self.e < o.e
        
        rooms = []
        waiting = []
        for i in range(n):
            heapq.heappush(rooms, Rooms(i))
        for i in meetings:
            heapq.heappush(waiting, Wait(i[0], i[1]))
        
        taken = []
        time = -1
        chk = {}
        while waiting:
            while taken and waiting[0].s >= taken[0].e:
                curr = heapq.heappop(taken)
                heapq.heappush(rooms, Rooms(curr.r))
            if rooms:
                curr = heapq.heappop(rooms)
                wait = heapq.heappop(waiting)
                duration = wait.e-wait.s
                time = max(time, wait.s)
                #print(curr.n, time, wait.s, wait.e)
                chk[curr.n] = chk.get(curr.n, 0)+1
                heapq.heappush(taken, Taken(time, time+duration, curr.n))
            else:
                earliest = taken[0].e
                time = max(time, earliest)
                while taken and earliest >= taken[0].e:
                    curr = heapq.heappop(taken)
                    #print(curr.r, earliest, '@')
                    heapq.heappush(rooms, Rooms(curr.r))
        #print(chk)
        res = -1
        m = -float('inf')
        for i in chk:
            if chk[i] > m:
                m = chk[i]
                res = i
        return res
        
            
                
                