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
                return self.f > o.f
        print(freq)
        import heapq
        pq = []
        for i in freq:
            heapq.heappush(pq, Tmp(i, freq[i]))
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq).val)
        return res