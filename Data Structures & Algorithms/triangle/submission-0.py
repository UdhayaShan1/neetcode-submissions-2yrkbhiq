class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def dfs(ind, level):
            if level >= len(triangle):
                return 0
            key = (ind, level)
            if key in dp:
                return dp[key]
            dp[key] = min(dfs(ind, level+1)+triangle[level][ind], dfs(ind+1, level+1)+triangle[level][ind])
            return dp[key]
        return dfs(0, 0)