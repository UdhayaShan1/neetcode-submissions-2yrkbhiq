class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import cache
        @cache
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return dfs(i+1, j+1)+1
            return max(dfs(i+1, j), dfs(i, j+1))
        return dfs(0, 0)