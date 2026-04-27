class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq
        class Tmp:
            def __init__(self, val):
                self.v = val
                self.diff = abs(val-x)
            def __lt__(self, o):
                return abs(self.diff) > abs(o.diff)
        
        pq = []
        for i in arr:
            if len(pq) == k:
                tmp = abs(i-x)
                if tmp < pq[0].diff:
                    heapq.heappop(pq)
                    heapq.heappush(pq, Tmp(i))
            else:
                heapq.heappush(pq, Tmp(i))
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq).v)
        res.sort()
        return res