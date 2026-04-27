class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def f(k):
            left = 0
            res = 0
            curr = 0
            for i in range(len(nums)):
                curr += nums[i]
                while left < len(nums) and curr > k:
                    curr -= nums[left]
                    left += 1
                res += max(i-left+1, 0)
            return res
        return f(goal)-f(goal-1)
