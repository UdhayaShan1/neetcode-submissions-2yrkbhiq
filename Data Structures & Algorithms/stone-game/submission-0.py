class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        t = sum(piles)
        from functools import cache
        @cache
        def dfs(i, j, a):
            if i > j:
                return 0
            if a:
                return max(dfs(i+1, j, not a)+piles[i], dfs(i, j-1, not a)+piles[j])
            return min(dfs(i+1, j, not a), dfs(i, j-1, not a))
        res = dfs(0, len(piles)-1, True)
        return True if res > t-res else False