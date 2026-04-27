class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        class Freq:
            def __init__(self, v, f):
                self.v = v
                self.f = f
            def __lt__(self, o):
                return self.f > o.f
        
        class Taken:
            def __init__(self, v, f, free):
                self.v = v
                self.f = f
                self.free = free
            def __lt__(self, o):
                return self.free < o.free
        
        c = {}
        for i in tasks:
            c[i] = c.get(i, 0)+1
        
        f = []
        t = []
        import heapq
        for i in c:
            heapq.heappush(f, Freq(i, c[i]))
        
        time = 0
        while f or t:
            if len(f) > 0:
                pop = heapq.heappop(f)
                if pop.f - 1 > 0:
                    heapq.heappush(t, Taken(pop.v, pop.f-1, time+n+1))
                time += 1

                while t and time >= t[0].free:
                    pop = heapq.heappop(t)
                    heapq.heappush(f, Freq(pop.v, pop.f))
            else:
                if time < t[0].free:
                    time = t[0].free
                
                while t and time >= t[0].free:
                    pop = heapq.heappop(t)
                    heapq.heappush(f, Freq(pop.v, pop.f))
        return time
                


    