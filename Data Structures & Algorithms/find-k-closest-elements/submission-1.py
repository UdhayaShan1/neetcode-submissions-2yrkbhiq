class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq
        class Tmp:
            def __init__(self, val):
                self.val = val
            def __lt__(self, o):
                return abs(self.val-x) > abs(o.val-x)
        
        pq = []
        for i in arr:
            if len(pq) < k:
                heapq.heappush(pq, Tmp(i))
            else:
                pop = heapq.heappop(pq)
                if abs(i-x) < abs(pop.val-x):
                    heapq.heappush(pq, Tmp(i))
                else:
                    heapq.heappush(pq, pop)
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq).val)
        res.sort()
        return res