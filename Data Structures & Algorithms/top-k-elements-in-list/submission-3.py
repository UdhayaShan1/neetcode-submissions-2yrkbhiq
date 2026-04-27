class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1+count.get(i, 0)
        
        pq = []
        import heapq
        class Tmp:
            def __init__(self, v, c):
                self.v = v
                self.c = c
            def __lt__(self, o):
                return self.c < o.c
        for i in count:
            heapq.heappush(pq, Tmp(i, count[i]))
            if len(pq) > k:
                heapq.heappop(pq)
        
        res = []
        while len(pq) > 0:
            res.append(heapq.heappop(pq).v)
        return res
