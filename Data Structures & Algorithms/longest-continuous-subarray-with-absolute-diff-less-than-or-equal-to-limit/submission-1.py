class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        class Min:
            def __init__(self, val, index):
                self.val = val
                self.index = index
            def __lt__(self, o):
                return self.val < o.val
        class Max:
            def __init__(self, val, index):
                self.val = val
                self.index = index
            def __lt__(self, o):
                return self.val > o.val
        
        import heapq
        maxpq = []
        minpq = []
        left = 0
        res = 0
        for i in range(len(nums)):
            ref = nums[i]
            heapq.heappush(maxpq, Max(ref, i))
            heapq.heappush(minpq, Min(ref, i))

            while maxpq and minpq and abs(maxpq[0].val-minpq[0].val) > limit:
                left += 1
                while maxpq and maxpq[0].index < left:
                    heapq.heappop(maxpq)
                while minpq and minpq[0].index < left:
                    heapq.heappop(minpq)
                
            #print(left, i)
            res = max(res, i-left+1)
        return res
            

            