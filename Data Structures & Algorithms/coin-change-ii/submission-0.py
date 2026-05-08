class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import cache
        @cache
        def dfs(k1, amt):
            if amt == 0:
                return 1
            if k1 >= len(coins) or amt < 0:
                return 0
            return dfs(k1, amt-coins[k1])+dfs(k1+1, amt)
        return dfs(0, amount)