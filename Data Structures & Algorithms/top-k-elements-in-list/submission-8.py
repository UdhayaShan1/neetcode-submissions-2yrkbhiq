class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        class Tmp:
            def __init__(self, n, c):
                self.n = n
                self.c = c
            def __lt__(self, o):
                return self.c < o.c
        c = {}
        for i in nums:
            c[i] = c.get(i, 0)+1
        for i in c:
            if len(pq) < k:
                heapq.heappush(pq, Tmp(i, c[i]))
            else:
                if pq[0].c < c[i]:
                    heapq.heappop(pq)
                    heapq.heappush(pq, Tmp(i, c[i]))
        
        res = []
        while pq:
            res.append(heapq.heappop(pq).n)
        return res
        