class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1+freq.get(i, 0)
        class Tmp:
            def __init__(self, val, f):
                self.val = val
                self.f = f
            def __lt__(self, o):
                return self.f < o.f
        #print(freq)
        import heapq
        pq = []
        for i in freq:
            if len(pq) < k:
                heapq.heappush(pq, Tmp(i, freq[i]))
            else:
                pop = heapq.heappop(pq)
                if pop.f < freq[i]:
                    heapq.heappush(pq, Tmp(i, freq[i]))
                else:
                    heapq.heappush(pq, pop)
        res = []
        for i in pq:
            res.append(i.val)
        return res

