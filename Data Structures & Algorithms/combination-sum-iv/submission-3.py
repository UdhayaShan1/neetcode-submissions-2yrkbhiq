class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def cache(func):
            dp = {}
            def wrapper(*args, **kwargs):
                key = (args, tuple(sorted(kwargs.items())))
                if key in dp:
                    return dp[key]
                dp[key] = func(*args, **kwargs)
                return dp[key]
            return wrapper
        @cache
        def dfs(n):
            if n == 0:
                return 1
            res = 0
            for i in nums:
                if n-i >= 0:
                    res += dfs(n-i)
            return res
        return dfs(target)
