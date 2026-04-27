class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        class Min:
            def __init__(self, v, i):
                self.v = v
                self.i = i
            def __lt__(self, o):
                return self.v < o.v
        class Max:
            def __init__(self, v, i):
                self.v = v
                self.i = i
            def __lt__(self, o):
                return self.v > o.v
        

        import heapq

        minq = []
        maxq = []
        left = 0
        res = 0
        for i in range(len(nums)):
            heapq.heappush(minq, Min(nums[i], i))
            heapq.heappush(maxq, Max(nums[i], i))

            while maxq and minq and maxq[0].v - minq[0].v > limit:
                left += 1
                while maxq and maxq[0].i < left:
                    heapq.heappop(maxq)
                while minq and minq[0].i < left:
                    heapq.heappop(minq)
            res = max(res, i-left+1)
        return res