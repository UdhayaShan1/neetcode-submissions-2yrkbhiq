class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        class Tmp:
            def __init__(self, v):
                self.v = v
            def __lt__(self, o):
                return self.v > o.v
        import heapq
        for i in stones:
            heapq.heappush(pq, Tmp(i))
        
        while len(pq) > 1:
            s1 = heapq.heappop(pq).v
            s2 = heapq.heappop(pq).v
            if s1 == s2:
                continue
            heapq.heappush(pq, Tmp(max(s1,s2)-min(s1,s2)))
        return 0 if len(pq) == 0 else pq[0].v

