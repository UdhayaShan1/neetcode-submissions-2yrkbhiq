class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        class Tmp:
            def __init__(self, val):
                self.val = val
            def __lt__(self, o):
                return self.val < o.val
        pq = []
        for i in nums:
            if len(pq) < k:
                heapq.heappush(pq, Tmp(i))
            else:
                if i <= pq[0].val:
                    continue
                heapq.heappop(pq)
                heapq.heappush(pq, Tmp(i))
        
        return pq[0].val
