class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        chk = {}
        for i in nums:
            chk[i] = chk.get(i, 0)+1
        pq = []
        import heapq

        class Tmp:
            def __init__(self, val, f):
                self.v = val
                self.f = f
            def __lt__(self, o):
                return self.f < o.f
        
        for i in chk:
            if len(pq) == k:
                if pq[0].f >= chk[i]:
                    continue
                heapq.heappop(pq)
            heapq.heappush(pq, Tmp(i, chk[i]))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq).v)
        return res
