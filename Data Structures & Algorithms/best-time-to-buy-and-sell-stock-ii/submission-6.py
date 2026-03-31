class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(k1, bought):
            if k1 >= len(prices):
                return 0
            res = -float('inf')
            key = (k1, bought)
            if key in dp:
                return dp[key]
            if not bought:
                res = max(res, dfs(k1+1, bought), dfs(k1+1, not bought)-prices[k1])
            else:
                res = max(res, dfs(k1+1, bought), dfs(k1+1, not bought)+prices[k1])
            dp[key] = res
            return res
        return dfs(0, False)