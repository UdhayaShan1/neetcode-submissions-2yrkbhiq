class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        def dfs(k1, n):
            if n == 0:
                return 0
            if n < 0 or k1**2 > n:
                return float('inf')
            key = (k1, n)
            if key in dp:
                return dp[key]
            dp[key] = min(dfs(k1, n-k1**2)+1, dfs(k1+1, n))
            return dp[key]
        return dfs(1, n)