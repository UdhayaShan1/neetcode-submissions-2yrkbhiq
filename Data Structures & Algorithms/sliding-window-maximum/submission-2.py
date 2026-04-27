class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq

        class Tmp:
            def __init__(self, v, i):
                self.i = i
                self.v = v
            def __lt__(self, o):
                return self.v > o.v
        
        pq = []
        left = 0
        right = k-1
        res = []
        for i in range(k):
            heapq.heappush(pq, Tmp(nums[i], i))
        while True:
            while pq and pq[0].i < left:
                heapq.heappop(pq)
            res.append(pq[0].v)
            if right+1 >= len(nums):
                break
            heapq.heappush(pq, Tmp(nums[right+1], right+1))
            left += 1
            right += 1
        return res
