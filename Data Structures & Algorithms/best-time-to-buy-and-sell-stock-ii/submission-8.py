class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(k1, bought):
            if k1 >= len(prices):
                return 0
            key = (k1, bought)
            if key in dp:
                return dp[key]
            if bought:
                dp[key] = max(dfs(k1+1, bought), dfs(k1+1, not bought)+prices[k1])
            else:
                dp[key] = max(dfs(k1+1, bought), dfs(k1+1, not bought)-prices[k1])
            return dp[key]
        return dfs(0, False)
                