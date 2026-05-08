class Solution:
    def climbStairs(self, n: int) -> int:
        def cache(func):
            dp = {}
            def wrapper(*args, **kwargs):
                key = (args, tuple(sorted(kwargs.items())))
                if key in dp:
                    return dp[key]
                dp[key] = func(*args, **kwargs)
                return dp[key]
            return wrapper

        class Cache:
            def __init__(self, func):
                self.func = func
                self.dp = {}
            def __call__(self, *args, **kwargs):
                key = (args, tuple(sorted(kwargs.items())))
                if key in self.dp:
                    return self.dp[key]
                self.dp[key] = self.func(*args, **kwargs)
                return self.dp[key]


        @Cache
        def dfs(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            return dfs(n-1)+dfs(n-2)
        return dfs(n)