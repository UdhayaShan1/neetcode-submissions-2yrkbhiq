class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        pq = []
        class Tmp:
            def __init__(self, val, index):
                self.v = val
                self.i = index
            def __lt__(self, o):
                return self.v > o.v
        
        for i in range(k):
            heapq.heappush(pq, Tmp(nums[i], i))
        
        res = []
        left = 0
        right = k-1
        while True:
            res.append(pq[0].v)
            if right+1 >= len(nums):
                return res
            left += 1
            heapq.heappush(pq, Tmp(nums[right+1], right+1))
            right += 1
            while pq[0].i < left:
                heapq.heappop(pq)
        return res
            