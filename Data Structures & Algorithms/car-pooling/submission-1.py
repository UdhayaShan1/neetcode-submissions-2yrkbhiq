class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        class Tmp:
            def __init__(self, n, f, t):
                self.n = n
                self.f = f
                self.t = t
            def __lt__(self, o):
                return self.f < o.f

        class Tmp1:
            def __init__(self, n, f, t):
                self.n = n
                self.f = f
                self.t = t
            def __lt__(self, o):
                return self.t < o.t
            

        trips.sort(key=lambda x:x[1])
        wait = []
        count = 0
        for i in range(len(trips)):
            while wait and trips[i][1] >= wait[0].t:
                tmp = heapq.heappop(wait)
                count -= tmp.n
            
            count += trips[i][0]
            if count > capacity:
                return False
            heapq.heappush(wait, Tmp1(trips[i][0], trips[i][1], trips[i][2]))
        return True

                 
                 





