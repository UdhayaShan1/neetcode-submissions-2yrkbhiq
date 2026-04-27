class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = deque()
        maxq = deque()
        class Num:
            def __init__(self, val, index):
                self.val = val
                self.index = index

        left = 0
        res = 0
        for i in range(len(nums)):
            ref = nums[i]

            while len(minq) > 0 and ref <= minq[-1].val:
                minq.pop()
            while len(maxq) > 0 and ref >= maxq[-1].val:
                maxq.pop()

            new = Num(ref, i)
            minq.append(new)
            maxq.append(new)
            
            while len(minq) > 0 and len(maxq) > 0 and abs(minq[0].val - maxq[0].val) > limit:
                left += 1
                while len(minq) > 0 and minq[0].index < left:
                    minq.popleft()
                while len(maxq) > 0 and maxq[0].index < left:
                    maxq.popleft() 
            res = max(res, i-left+1)
        return res
            

                

            
