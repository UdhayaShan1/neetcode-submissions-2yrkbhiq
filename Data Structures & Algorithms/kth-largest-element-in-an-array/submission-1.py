class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        class Tmp:
            def __init__(self, val):
                self.v = val
            def __lt__(self, o):
                return self.v < o.v
        pq = []
        import heapq
        for i in range(len(nums)):
            if len(pq) < k:
                heapq.heappush(pq, Tmp(nums[i]))
            else:
                if nums[i] > pq[0].v:
                    heapq.heappop(pq)
                    heapq.heappush(pq, Tmp(nums[i]))
        return pq[0].v