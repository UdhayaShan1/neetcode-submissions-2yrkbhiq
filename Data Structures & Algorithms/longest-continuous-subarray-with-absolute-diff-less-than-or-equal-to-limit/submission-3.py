class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = deque()
        maxq = deque()
        left = 0
        res = 0
        for i in range(len(nums)):
            while minq and minq[-1][1] >= nums[i]:
                minq.pop()
            while maxq and maxq[-1][1] <= nums[i]:
                maxq.pop()
            
            minq.append((i, nums[i]))
            maxq.append((i, nums[i]))

            while minq and maxq and abs(minq[0][1]-maxq[0][1]) > limit:
                left += 1
                while minq and minq[0][0] < left:
                    minq.popleft()
                while maxq and maxq[0][0] < left:
                    maxq.popleft()
            res = max(res, i-left+1)
        return res
     

