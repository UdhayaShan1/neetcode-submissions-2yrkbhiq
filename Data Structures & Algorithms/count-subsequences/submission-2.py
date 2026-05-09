class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            key = (i, j)
            if key in dp:
                return dp[key]
            if s[i] == t[j]:
                dp[key] = dfs(i+1, j) + dfs(i+1, j+1)
            else:
                dp[key] = dfs(i+1, j)
            return dp[key]
        return dfs(0, 0)