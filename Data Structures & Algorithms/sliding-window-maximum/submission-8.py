class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        class Tmp:
            def __init__(self, pos, val):
                self.p = pos
                self.v = val
            def __lt__(self, o):
                return self.v > o.v
        
        pq = []
        for i in range(k):
            heapq.heappush(pq, Tmp(i, nums[i]))
        
        res = []
        left = 0
        right = k-1
        while True:
            while pq and pq[0].p < left:
                heapq.heappop(pq)
            res.append(pq[0].v)
            if right+1 >= len(nums):
                return res
            left += 1
            heapq.heappush(pq, Tmp(right+1, nums[right+1]))
            right += 1
