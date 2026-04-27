class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        import heapq
        chk = {}
        class Tmp:
            def __init__(self, v, c):
                self.v = v
                self.c = c
            def __lt__(self, o):
                return self.c > o.c
        for i in nums:
            if i not in chk:
                chk[i] = 0
            chk[i] += 1

            heapq.heappush(pq, Tmp(i, chk[i]))
        
        res = []
        chk = {}
        while len(pq) > 0:
            curr = heapq.heappop(pq)
            if len(res) > 0 and curr.v in chk:
                continue
            chk[curr.v] = 1
            res.append(curr.v)
 
        
        return res[:k]