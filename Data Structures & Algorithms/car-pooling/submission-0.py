class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        class E:
            def __init__(self, p, f, t):
                self.p = p
                self.f = f
                self.t = t
            def __lt__(self, o):
                return self.f < o.f
    
        class E2:
            def __init__(self, p, f, t):
                self.p = p
                self.f = f
                self.t = t
            def __lt__(self, o):
                return self.t < o.t
        
        import heapq 
        loc = 0
        curr = 0
        pq = []
        arr = []
        for i in trips:
            arr.append(E(i[0], i[1], i[2]))
        arr.sort()

        for i in range(len(arr)):
            while pq and pq[0].t <= arr[i].f:
                curr -= heapq.heappop(pq).p
            
            curr += arr[i].p
            if curr > capacity:
                return False
            heapq.heappush(pq, E2(arr[i].p, arr[i].f, arr[i].t))
        return True
            



                
