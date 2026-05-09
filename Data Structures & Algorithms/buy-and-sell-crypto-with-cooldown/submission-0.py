class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache
        @cache
        def dfs(k1, bought):
            if k1 >= len(prices):
                return 0
            if bought:
                return max(dfs(k1+2, False)+prices[k1], dfs(k1+1, bought))
            return max(dfs(k1+1, True)-prices[k1], dfs(k1+1, bought))
        return dfs(0, False)