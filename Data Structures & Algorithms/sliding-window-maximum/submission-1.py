class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        i = 0
        while i < len(nums):
            while dq and dq[0]+k <= i:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:  # use <= to prefer newer equal vals
                dq.pop()
            dq.append(i)
            if dq[-1] >= k-1:
                res.append(nums[dq[0]])
            i += 1
        return res

                 