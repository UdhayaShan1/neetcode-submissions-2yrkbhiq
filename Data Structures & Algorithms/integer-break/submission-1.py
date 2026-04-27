class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def dfs(no, n, two):
            if n == 0:
                return 1 if two == 2 else 0
            if n < 0 or no > n:
                return 0
            key = (no, n, two)
            if key in dp:
                return dp[key]
            
            dp[key] = max(dfs(no, n-no, min(2, two+1))*no, dfs(no+1, n, two))
            return dp[key]
        return dfs(1, n, 0)


        