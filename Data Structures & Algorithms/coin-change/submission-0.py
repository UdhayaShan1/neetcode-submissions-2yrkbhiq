class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(k1, amt):
            if amt == 0:
                return 0
            if k1 >= len(coins) or amt < 0:
                return float('inf')
            key = (k1, amt)
            if key in dp:
                return dp[key]
            dp[key] = min(dfs(k1, amt-coins[k1])+1, dfs(k1+1, amt))
            return dp[key]
        res = dfs(0, amount)
        return res if res != float('inf') else -1