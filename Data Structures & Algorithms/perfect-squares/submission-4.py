class Solution:
    def numSquares(self, n: int) -> int:
        sys.setrecursionlimit(999999)
        from functools import cache
        @cache
        def dfs(k1, curr):
            if curr == n:
                return 0
            if curr > n or k1**2 > n:
                return float('inf')
            
            return min(dfs(k1, curr+k1**2)+1, dfs(k1+1, curr))
        return dfs(1, 0)
