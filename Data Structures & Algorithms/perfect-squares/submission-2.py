class Solution:
    def numSquares(self, n: int) -> int:
        from functools import cache
        sys.setrecursionlimit(99999)

        @cache
        def dfs(k1, n):
            if n == 0:
                return 0
            if k1**2 > n or n < 0:
                return float('inf')

            return min(dfs(k1, n-k1**2)+1, dfs(k1+1, n))
        return dfs(1, n)
