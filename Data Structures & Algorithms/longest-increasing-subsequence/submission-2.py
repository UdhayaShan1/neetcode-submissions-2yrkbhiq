class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sys.setrecursionlimit(99999)
        from functools import cache
        @cache
        def dfs(k1, prev):
            if k1 >= len(nums):
                return 0
            res = -float('inf')
            if prev is not None and nums[k1] <= nums[prev]:
                res = max(res, dfs(k1+1, prev))
            else:
                res = max(res, dfs(k1+1, prev), dfs(k1+1, k1)+1)
            return res
        return dfs(0, None)
            