class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        class Tmp:
            def __init__(self, c, count):
                self.c = c
                self.count = count
            def __lt__(self, o):
                return self.count > o.count
        
        pq = []
        if a:
            heapq.heappush(pq, Tmp('a', a))
        if b:
            heapq.heappush(pq, Tmp('b', b))
        if c:
            heapq.heappush(pq, Tmp('c', c))
        res = ""
        while pq:
            ref = heapq.heappop(pq)
            if len(res) > 1 and res[-2] == res[-1] and res[-1] == ref.c:
                if not pq:
                    break
                ref2 = heapq.heappop(pq)
                res += ref2.c
                heapq.heappush(pq, Tmp(ref.c, ref.count))
                if ref2.count-1 > 0:
                    heapq.heappush(pq, Tmp(ref2.c, ref2.count-1))
            else:
                res += ref.c
                if ref.count-1 > 0:
                    heapq.heappush(pq, Tmp(ref.c, ref.count-1))
        return res



        