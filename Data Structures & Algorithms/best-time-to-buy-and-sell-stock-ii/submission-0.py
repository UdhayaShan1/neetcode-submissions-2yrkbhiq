class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(k1, sold):
            if k1 >= len(prices):
                return 0
            key = (k1, sold)
            if key in dp:
                return dp[key]
            if sold:
                dp[key] = max(dfs(k1+1, sold), dfs(k1+1, not sold)+prices[k1])
            else:
                dp[key] = max(dfs(k1+1, sold), dfs(k1+1, not sold)-prices[k1])
            return dp[key]
        return dfs(0, False)