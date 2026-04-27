class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        class Tmp:
            def __init__(self, v, f):
                self.v = v
                self.f = f
            def __lt__(self, o):
                return self.f < o.f
        
        import heapq
        pq = []
        d = {}
        for i in nums:
            d[i] = d.get(i, 0)+1
        for i in d:
            if len(pq) < k:
                heapq.heappush(pq, Tmp(i, d[i]))
            else:
                if d[i] > pq[0].f:
                    heapq.heappop(pq)
                    heapq.heappush(pq, Tmp(i, d[i]))
        res = []
        while pq:
            res.append(heapq.heappop(pq).v)
        return res
