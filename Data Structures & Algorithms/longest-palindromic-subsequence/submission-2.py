class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        sys.setrecursionlimit(9999999)
        from functools import cache
        @cache
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            res = max(dfs(i+1, j-1), dfs(i+1, j), dfs(i, j-1))
            if s[i] == s[j]:
                res = max(res, dfs(i+1, j-1)+2)
            return res
        return dfs(0, len(s)-1)