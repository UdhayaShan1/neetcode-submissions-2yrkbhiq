class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from functools import cache

        @cache
        def dfs(k1, t):
            if k1 >= len(nums):
                return 1 if t == 0 else 0
            return dfs(k1+1, t-nums[k1])+dfs(k1+1, t+nums[k1])
        return dfs(0, target)