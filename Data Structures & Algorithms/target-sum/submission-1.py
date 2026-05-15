class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from functools import cache
        @cache
        def dfs(k1, curr):
            if k1 >= len(nums):
                return 1 if curr == target else 0
            return dfs(k1+1, curr+nums[k1])+dfs(k1+1, curr-nums[k1])
        return dfs(0, 0)
